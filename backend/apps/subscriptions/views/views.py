import logging

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from djstripe.enums import SubscriptionStatus
from djstripe.settings import djstripe_settings
from stripe.error import InvalidRequestError

from ..decorators import redirect_subscription_errors, active_subscription_required
from ..wrappers import SubscriptionWrapper, InvoiceFacade
from ..forms import UsageRecordForm
from ..helpers import get_subscription_urls, subscription_is_active, subscription_is_trialing
from apps.teams.decorators import team_admin_required, login_and_team_required
from ..models import SubscriptionModelBase
from apps.utils.billing import get_stripe_module

log = logging.getLogger("my_app.subscription")


@redirect_subscription_errors
@team_admin_required
def subscription(request, team_slug):
    subscription_holder = request.team
    if subscription_holder.has_active_subscription():
        return _view_subscription(request, subscription_holder)
    else:
        return _upgrade_subscription(request, subscription_holder)


def _view_subscription(request, subscription_holder: SubscriptionModelBase):
    """
    Show user's active subscription
    """
    assert subscription_holder.has_active_subscription()
    subscription = subscription_holder.active_stripe_subscription
    next_invoice = None
    if subscription_is_trialing(subscription) and not subscription.default_payment_method:
        # trialing subscriptions with no payment method set don't have invoices so we can skip that check
        pass
    elif not subscription.cancel_at_period_end:
        stripe = get_stripe_module()
        try:
            next_invoice = stripe.Invoice.upcoming(
                subscription=subscription.id,
            )
        except InvalidRequestError:
            # this error is raised if you try to get an invoice but the subscription is canceled or deleted
            # check if this happened and redirect to the upgrade page if so
            subscription_is_invalid = False
            try:
                stripe_subscription = stripe.Subscription.retrieve(subscription.id)
            except InvalidRequestError:
                log.error(
                    "The subscription could not be retrieved from Stripe. "
                    "If you are running in test mode, it may have been deleted."
                )
                stripe_subscription = None
                subscription_holder.subscription = None
                subscription_holder.save()
                subscription_is_invalid = True
            if stripe_subscription and (
                stripe_subscription.status != SubscriptionStatus.active or stripe_subscription.cancel_at_period_end
            ):
                log.warning(
                    "A canceled subscription was not synced to your app DB. "
                    "Your webhooks may not be set up properly. "
                    "See: https://docs.saaspegasus.com/subscriptions.html#webhooks"
                )
                # update the subscription in the database and clear from the subscription_holder
                subscription.sync_from_stripe_data(stripe_subscription)
                subscription_is_invalid = True
            elif stripe_subscription:
                # failed for some other unexpected reason.
                raise

            if subscription_is_invalid:
                subscription_holder.refresh_from_db()
                subscription_holder.clear_cached_subscription()

                if not subscription_is_active(subscription):
                    return _upgrade_subscription(request, subscription_holder)

    wrapped_subscription = SubscriptionWrapper(subscription_holder.active_stripe_subscription)
    return render(
        request,
        "subscriptions/view_subscription.html",
        {
            "active_tab": "subscription",
            "page_title": _("Subscription | {team}").format(team=request.team),
            "subscription": wrapped_subscription,
            "next_invoice": InvoiceFacade(next_invoice) if next_invoice else None,
            "subscription_urls": get_subscription_urls(subscription_holder),
        },
    )


def _upgrade_subscription(request, subscription_holder: SubscriptionModelBase):
    return render(
        request,
        "subscriptions/upgrade_subscription.html",
        {
            "active_tab": "subscription",
            "stripe_public_key": djstripe_settings.STRIPE_PUBLIC_KEY,
            "stripe_pricing_table_id": settings.STRIPE_PRICING_TABLE_ID,
            "client_reference_id": subscription_holder.id,
        },
    )


@login_and_team_required
def subscription_demo(request, team_slug):
    subscription_holder = request.team
    subscription = subscription_holder.active_stripe_subscription
    wrapped_subscription = SubscriptionWrapper(subscription) if subscription else None
    return render(
        request,
        "subscriptions/demo.html",
        {
            "active_tab": "subscription_demo",
            "subscription": wrapped_subscription,
            "subscription_urls": get_subscription_urls(subscription_holder),
            "page_title": _("Subscription Demo | {team}").format(team=request.team),
        },
    )


@login_and_team_required
@active_subscription_required
def subscription_gated_page(request, team_slug):
    return render(request, "subscriptions/subscription_gated_page.html")


@login_and_team_required
@active_subscription_required
def metered_billing_demo(request, team_slug):
    subscription_holder = request.team
    if request.method == "POST":
        form = UsageRecordForm(subscription_holder, request.POST)
        if form.is_valid():
            usage_data = form.save()
            messages.info(request, _("Successfully recorded {} units for metered billing.").format(usage_data.quantity))
            return HttpResponseRedirect(reverse("subscriptions_team:subscription_demo", args=[team_slug]))
    else:
        form = UsageRecordForm(subscription_holder)

    if not form.is_usable():
        messages.info(
            request,
            _(
                "It looks like you don't have any metered subscriptions set up. "
                "Sign up for a subscription with metered usage to use this UI."
            ),
        )
    return render(
        request,
        "subscriptions/metered_billing_demo.html",
        {
            "subscription": subscription_holder.active_stripe_subscription,
            "form": form,
        },
    )

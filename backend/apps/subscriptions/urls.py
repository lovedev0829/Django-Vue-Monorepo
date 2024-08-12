from django.urls import path

from . import views

app_name = "subscriptions"

urlpatterns = [
    path("api/active-products/", views.ProductWithMetadataAPI.as_view(), name="products_api"),
    path("confirm/", views.subscription_confirm, name="subscription_confirm"),
]

team_urlpatterns = (
    [
        path("", views.subscription, name="subscription_details"),
        path("demo/", views.subscription_demo, name="subscription_demo"),
        path("subscription-gated-page/", views.subscription_gated_page, name="subscription_gated_page"),
        path("metered-billing-demo/", views.metered_billing_demo, name="metered_billing_demo"),
        # stripe checkout views
        path("checkout-canceled/", views.checkout_canceled, name="checkout_canceled"),
        # stripe integration views that return redirects to Stripe
        # these are the defaults
        path("stripe/portal/", views.create_portal_session, name="create_stripe_portal_session"),
        # stripe api views that return Stripe URLs instead of redirects
        # these can be used by JavaScript front-ends to handle the redirect from the response
        path(
            "stripe/api/create-checkout-session/",
            views.CreateCheckoutSession.as_view(),
            name="api_create_checkout_session",
        ),
        path(
            "stripe/api/create-portal-session/", views.CreatePortalSession.as_view(), name="api_create_portal_session"
        ),
    ],
    "subscriptions_team",
)

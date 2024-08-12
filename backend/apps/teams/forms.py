from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Invitation, Membership
from .helpers import create_default_team_for_user
from apps.users.forms import TurnstileSignupForm


class TeamSignupForm(TurnstileSignupForm):
    invitation_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    team_name = forms.CharField(
        label=_("Team Name (Optional)"),
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": _("Team Name (Optional)")}),
        required=False,
    )
    terms_agreement = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # blank out overly-verbose help text
        self.fields["password1"].help_text = ""
        link = '<a class="link" href={} target="_blank">{}</a>'.format(
            reverse("web:terms"),
            _("Terms and Conditions"),
        )
        self.fields["terms_agreement"].label = mark_safe(_("I agree to the {terms_link}").format(terms_link=link))

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            self._clean_team_name(cleaned_data)
            self._clean_invitation_email(cleaned_data)
        return cleaned_data

    def _clean_team_name(self, cleaned_data):
        team_name = cleaned_data.get("team_name")
        invitation_id = cleaned_data.get("invitation_id")
        # if invitation is not set then team name is required
        if not invitation_id and not team_name:
            email = cleaned_data.get("email")
            if email is not None:
                team_name = f"{email.split('@')[0]}"
        elif invitation_id:
            assert not team_name

        cleaned_data["team_name"] = team_name

    def _clean_invitation_email(self, cleaned_data):
        invitation_id = cleaned_data.get("invitation_id")
        if invitation_id:
            try:
                invite = Invitation.objects.get(id=invitation_id)
            except (Invitation.DoesNotExist, ValidationError):
                # ValidationError is raised if the ID isn't a valid UUID, which should be treated the same
                # as not found
                raise forms.ValidationError(
                    _(
                        "That invitation could not be found. "
                        "Please double check your invitation link or sign in to continue."
                    )
                )

            if invite.is_accepted:
                raise forms.ValidationError(
                    _(
                        "It looks like that invitation link has expired. "
                        "Please request a new invitation or sign in to continue."
                    )
                )

            email = cleaned_data.get("email")
            if invite.email != email:
                raise forms.ValidationError(
                    _("You must sign up with the email address that the invitation was sent to.")
                )

    def save(self, request):
        invitation_id = self.cleaned_data["invitation_id"]
        team_name = self.cleaned_data["team_name"]
        user = super().save(request)

        # if the account already exists, the super().save call is empty, so don't do any post-processing
        if not user:
            return

        if not invitation_id:
            create_default_team_for_user(user, team_name)

        return user


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ("role",)

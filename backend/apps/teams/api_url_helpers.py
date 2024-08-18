from django.urls import reverse
from typing import Dict

TEAM_PLACEHOLDER = "__team_slug__"
INVITATION_PLACEHOLDER = "__invite_id__"
MEMBERSHIP_PLACEHOLDER = "__membership_id__"


def get_team_api_url_templates() -> Dict[str, str]:
    team_api_url_templates = {
        "single_team:manage_team": reverse("single_team:manage_team", args=[TEAM_PLACEHOLDER]),
    }
    invite_api_url_names = [
        "single_team:resend_invitation",
    ]
    membership_api_url_names = [
        "single_team:team_membership_details",
    ]
    invitation_url_templates = {
        api_url: reverse(api_url, args=[TEAM_PLACEHOLDER, INVITATION_PLACEHOLDER]) for api_url in invite_api_url_names
    }
    tmp_integer_url_key = 999999
    membership_url_templates = {
        api_url: reverse(api_url, args=[TEAM_PLACEHOLDER, tmp_integer_url_key]) for api_url in membership_api_url_names
    }
    membership_url_templates = {
        url_name: url.replace(str(tmp_integer_url_key), MEMBERSHIP_PLACEHOLDER)
        for url_name, url in membership_url_templates.items()
    }

    return {**team_api_url_templates, **invitation_url_templates, **membership_url_templates}

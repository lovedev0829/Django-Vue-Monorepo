# socialaccount/credentials.py

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from attrs import define

@define
class GoogleRawLoginCredentials:
    client_id: str
    client_secret: str

def google_raw_login_get_credentials() -> GoogleRawLoginCredentials:
    
    # client_id = settings.GOOGLE_OAUTH2_CLIENT_ID
    # client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET
    
    client_id = "683692295172-n7hkg8ca7ftgkknl4e3hbmjd0k8qqghf.apps.googleusercontent.com"
    client_secret = "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"

    if not client_id or not client_secret:
        raise ImproperlyConfigured("Google OAuth2 credentials are not properly configured.")

    return GoogleRawLoginCredentials(client_id=client_id, client_secret=client_secret)

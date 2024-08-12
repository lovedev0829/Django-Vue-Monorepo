    
from socialaccount.providers.google.views import GoogleOAuth2Adapter
from socialaccount.providers.github.views import GitHubOAuth2Adapter
from socialaccount.providers.slack.views import SlackOAuth2Adapter
from socialaccount.providers.trello.views import TrelloOAuthAdapter

from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    
class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    
class SlackLogin(SocialLoginView):
    adapter_class = SlackOAuth2Adapter

class TrelloLogin(SocialLoginView):
    adapter_class = TrelloOAuthAdapter
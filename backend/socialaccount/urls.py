from .views import GoogleLogin, SlackLogin, GithubLogin, TrelloLogin

from django.urls import path

urlpatterns = [
    path('google/auth/login/', GoogleLogin.as_view(), name='google_login'),
    path('slack/auth/login/', SlackLogin.as_view(), name='slack_login'),
    path('github/auth/login/', GithubLogin.as_view(), name='github_login'),
    path('trello/auth/login/', TrelloLogin.as_view(), name='trello_login'),
]
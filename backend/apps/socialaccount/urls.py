# from django.urls import path
# from .views  import GoogleLoginRedirectApi, GoogleLoginCallbackApi

# urlpatterns = [
#     path('google/auth/login/', GoogleLoginRedirectApi.as_view(), name='google_login'),
#     path('google/auth/callback/', GoogleLoginCallbackApi.as_view(), name='google_callback'),
# ]


from django.urls import path
from .views import GoogleLogin

urlpatterns = [
    path('google/auth/login/', GoogleLogin.as_view(), name='google_login'),
]
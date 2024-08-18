from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path("api/v1/", include("apps.authentication.urls")),
    path("api/v1/users/", include("apps.users.urls")),
    path("api/v1/teams/", include("apps.teams.urls")),
    path("api/v1/third-party/", include("apps.socialaccount.urls")),    
]

if settings.ENABLE_DEBUG_TOOLBAR:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))

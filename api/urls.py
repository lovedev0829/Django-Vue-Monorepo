from django.urls import path, include
from api.core.v1 import route as api_v1


urlpatterns = [
    path("v1/", include(api_v1.urls))  
]
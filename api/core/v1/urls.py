from rest_framework import routers
from api.core.v1.viewsets import *


route = routers.DefaultRouter()
route.register(r"notes", NoteViewSet, basename="notes")

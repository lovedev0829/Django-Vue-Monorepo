from django.urls import path
from . import views

app_name = "teams"

urlpatterns = [
    # Team URLs
    path("create", views.TeamViewSet.as_view({'post': 'create'}), name='team-create'),
    path("list/", views.TeamViewSet.as_view({'get': 'list'}), name='team-list'),
    path("retrieve/<int:pk>/", views.TeamViewSet.as_view({'get': 'retrieve'}), name='team-retrieve'),
    path("update/<int:pk>/", views.TeamViewSet.as_view({'put': 'update'}), name='team-update'),
    path("partial-update/<int:pk>/", views.TeamViewSet.as_view({'patch': 'partial_update'}), name='team-partial-update'),
    path("destroy/<int:pk>/", views.TeamViewSet.as_view({'delete': 'destroy'}), name='team-destroy'),

    # Invitation URLs
    path("invitations/create/", views.InvitationViewSet.as_view({'post': 'create'}), name='invitation-create'),
    path("invitations/list/", views.InvitationViewSet.as_view({'get': 'list'}), name='invitation-list'),
    path("invitations/retrieve/<int:pk>/", views.InvitationViewSet.as_view({'get': 'retrieve'}), name='invitation-retrieve'),
    path("invitations/update/<int:pk>/", views.InvitationViewSet.as_view({'put': 'update'}), name='invitation-update'),
    path("invitations/partial-update/<int:pk>/", views.InvitationViewSet.as_view({'patch': 'partial_update'}), name='invitation-partial-update'),
    path("invitations/destroy/<int:pk>/", views.InvitationViewSet.as_view({'delete': 'destroy'}), name='invitation-destroy'),
]

from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied, ValidationError as DRFValidationError
from rest_framework.decorators import api_view
from apps.api.permissions import IsAuthenticatedOrHasUserAPIKey

from ..invitations import send_invitation
from ..models import Team, Invitation
from ..permissions import TeamAccessPermissions, TeamModelAccessPermissions
from ..roles import is_admin, is_member
from ..serializers import TeamSerializer, InvitationSerializer
from ..constants import TenantUserRole
from rest_framework.response import Response
from apps.utils.hashid import encode, decode

@extend_schema_view(
    create=extend_schema(operation_id="teams_create"),
    list=extend_schema(operation_id="teams_list"),
    # retrieve=extend_schema(operation_id="teams_retrieve"),
    update=extend_schema(operation_id="teams_update"),
    partial_update=extend_schema(operation_id="teams_partial_update"),
    destroy=extend_schema(operation_id="teams_destroy"),
)
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrHasUserAPIKey, TeamAccessPermissions)

    def get_queryset(self):
        # filter queryset based on logged in user
        return self.request.user.teams.order_by("name")

    def perform_create(self, serializer):
        # ensure logged in user is set on the model during creation
        team = serializer.save()
        team.members.add(self.request.user, through_defaults={"role": TenantUserRole.OWNER})
    
    @api_view(['GET'])
    def retrieve(request, teamId):
        # Attempt to retrieve the team by its ID
        try:
            team = Team.objects.get(id=teamId)
            serializer = TeamSerializer(team, context={'request': request})
            return Response({'team': serializer.data})
        except Team.DoesNotExist:
            return Response({'error': 'Team not found'}, status=404)
    
    @api_view(['PUT'])
    def update(request, id):
        try:
            # Ensure you're working with the request object provided by DRF
            team = get_object_or_404(Team, id=id)

            # Get the 'name' from the request data (use request.data for POST/PUT/PATCH)
            name = request.data.get('name', None)
            
            if name:
                # Update the team name and save the changes
                team.name = name
                team.save()
                return Response({'message': "Team updated successfully!"})
            else:
                return Response({'error': 'Name not provided'}, status=400)
        
        except Team.DoesNotExist:
            return Response({'error': 'Team not found'}, status=404)
    
    @api_view(['delete'])
    def destroy(request, id):
        # Attempt to retrieve the team by its ID
        team = get_object_or_404(Team, id=id)
        
        # Delete the team from the database
        team.delete()
        
        # Return a success response
        return Response({'message': 'Team deleted successfully!'}, status=200)  # 204 No Content
        
        
    
@extend_schema(tags=["teams"])
@extend_schema_view(
    create=extend_schema(operation_id="invitations_create"),
    list=extend_schema(operation_id="invitations_list"),
    retrieve=extend_schema(operation_id="invitations_retrieve"),
    update=extend_schema(operation_id="invitations_update"),
    partial_update=extend_schema(operation_id="invitations_partial_update"),
    destroy=extend_schema(operation_id="invitations_destroy"),
)

class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    permission_classes = (IsAuthenticatedOrHasUserAPIKey, TeamModelAccessPermissions)

    @property
    def team(self):
        team = get_object_or_404(Team, slug=self.kwargs["team_slug"])
        if is_member(self.request.user, team):
            return team
        else:
            raise PermissionDenied()

    def _ensure_team_match(self, team):
        if team != self.team:
            raise DRFValidationError("Team set in invitation must match URL")

    def _ensure_no_pending_invite(self, team, email):
        if Invitation.objects.filter(team=team, email=email, is_accepted=False):
            raise DRFValidationError(
                {
                    "email": [
                        _(
                            'There is already a pending invitation for {}. You can resend it by clicking "Resend Invitation".'
                        ).format(email)
                    ]
                }
            )

    def get_queryset(self):
        return self.queryset.filter(team=self.team)

    def perform_create(self, serializer):
        team = serializer.validated_data["team"]
        self._ensure_team_match(team)
        self._ensure_no_pending_invite(team, serializer.validated_data["email"])

        if not is_admin(self.request.user, team):
            raise PermissionDenied()

        invitation = serializer.save(invited_by=self.request.user)
        send_invitation(invitation)
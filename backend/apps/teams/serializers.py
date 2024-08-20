from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.subscriptions.serializers import SubscriptionSerializer
from django.conf import settings
from .helpers import get_next_unique_team_slug
from .models import Team, Membership, Invitation
from .roles import is_admin, is_owner
from . import constants


class MembershipSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user.id")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    display_name = serializers.ReadOnlyField(source="user.get_display_name")

    class Meta:
        model = Membership
        fields = ("id", "user_id", "first_name", "last_name", "display_name", "role")


class InvitationSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    invited_by = serializers.ReadOnlyField(source="invited_by.get_display_name")

    class Meta:
        model = Invitation
        fields = ("id", "team", "email", "role", "invited_by", "is_accepted")


class TeamSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        required=False,
        validators=[UniqueValidator(queryset=Team.objects.all())],
    )
    members = MembershipSerializer(source="sorted_memberships", many=True, read_only=True)
    invitations = InvitationSerializer(many=True, read_only=True, source="pending_invitations")
    is_admin = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    subscription = SubscriptionSerializer(source="wrapped_subscription", read_only=True)
    
    # Set creator and type as read-only since they are set in the create method
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    type = serializers.CharField(read_only=True)
    
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "slug",
            "members",
            "creator",
            "type",
            "invitations",
            "is_admin",
            "is_owner",
            "subscription",
            "has_active_subscription",
        )

    def get_is_admin(self, obj) -> bool:
        return is_admin(self.context["request"].user, obj)
    
    def get_is_owner(self, obj) -> bool:
        return is_owner(self.context["request"].user, obj)

    def create(self, validated_data):
        team_name = validated_data.get("name", None)
        validated_data["slug"] = validated_data.get("slug", get_next_unique_team_slug(team_name))
        validated_data["creator"] = self.context["request"].user
        validated_data["type"] = constants.TenantType.ORGANIZATION
        
        return super().create(validated_data)

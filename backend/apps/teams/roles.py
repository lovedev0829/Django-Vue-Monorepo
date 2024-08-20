from __future__ import annotations

from apps.users.models import CustomUser
from . import constants

ROLE_CHOICES = (
    # customize roles here
    (constants.TenantUserRole.ADMIN, "Administrator"),
    (constants.TenantUserRole.MEMBER, "Member"),
    (constants.TenantUserRole.OWNER, "Owner"),
)

def is_member(user: CustomUser, team) -> bool:
    if not team:
        return False
    return team.members.filter(id=user.id).exists()

def is_owner(user: CustomUser, team) -> bool:
    if not team:
        return False

    from .models import Membership

    return Membership.objects.filter(team=team, user=user, role=constants.TenantUserRole.OWNER).exists()

def is_admin(user: CustomUser, team) -> bool:
    if not team:
        return False

    from .models import Membership

    return Membership.objects.filter(team=team, user=user, role=constants.TenantUserRole.ADMIN).exists()

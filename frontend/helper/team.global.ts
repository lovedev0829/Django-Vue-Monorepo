import { useTeamStore } from '@/stores/team';
import { TeamUserRole } from '@/constants/team.global';

export const generateTeamPath = (url: string, params: Record<string, any> = {}): string => {
    const { $router } = useNuxtApp();
    const teamStore = useTeamStore();

    const tenantId = teamStore.selectedTeam?.id ?? '';
    const fullPath = url ? `/${tenantId}/${url}` : `/${tenantId}`;
    
    return $router.resolve({ path: fullPath, query: params }).href;
};

export const checkTeamPermission = (allowedRoles: TeamUserRole[]): boolean => {
    const teamStore = useTeamStore();
    const currentTeamRole = teamStore.selectedTeam.role as TeamUserRole
    return allowedRoles.includes(currentTeamRole);
};

export const getCurrentTeamRole = (currentTeam: any): TeamUserRole => {
    
    if (currentTeam?.is_owner) {
        return TeamUserRole.OWNER;
    }
    
    if (currentTeam?.is_admin) {
        return TeamUserRole.ADMIN;
    }

    return TeamUserRole.MEMBER;
};

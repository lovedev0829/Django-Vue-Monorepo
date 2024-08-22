import { useTeamStore } from '@/stores/team';
import { TeamUserRole } from '@/constants/team.global';

export const generateTeamPath = (url: string, params: any) => {
    const { $router } = useNuxtApp();
  
    const teamStore = useTeamStore();
    const tenantId = teamStore.selectedTeam?.id ?? '';
    const fullPath = url ?  `/${tenantId}/${url}` : `/${tenantId}`;
    return $router.resolve({ path: fullPath, query: {  ...params } }).href;
    
}
  
// check Permission 

export const checkTeamPermission = (allowedRoles: TeamUserRole[]): boolean => {
    const teamStore = useTeamStore();

    // Determine the current role based on selectedTeam properties
    let currentTeamUserRole: TeamUserRole;

    if (teamStore.selectedTeam?.is_owner) {
        currentTeamUserRole = TeamUserRole.OWNER;
    } else if (teamStore.selectedTeam?.is_admin) {
        currentTeamUserRole = TeamUserRole.ADMIN;
    } else {
        currentTeamUserRole = TeamUserRole.MEMBER;
    }

    // Check if the user's role is in the allowedRoles array
    return allowedRoles.includes(currentTeamUserRole);
};
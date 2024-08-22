export enum TeamType {
    PERSONAL = 'default',
    ORGANIZATION = 'organization',
}

export enum TeamUserRole {
  ADMIN = 'admin',
  MEMBER = 'memeber',
  OWNER = 'owner'
}

export const CURRENT_TEAM_STORAGE_KEY = 'currentTeam';

export const generateTeamPath = (teamId: string) => {
  
}
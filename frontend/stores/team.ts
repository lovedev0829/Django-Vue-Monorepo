import { defineStore } from 'pinia';
import TeamService from "../services/TeamService";
import { CURRENT_TEAM_STORAGE_KEY, TeamType } from "@/constants/team.global";
import { getCurrentTeamRole } from '~/helper/team.global';

interface ICurrentTeam {
    id: string;
    role: string;
    type: string;
}

export const useTeamStore = defineStore('teams', {
  state: () => ({
    teams: [] as any[], // Define type for teams array
    selectedTeam: {} as ICurrentTeam, // Initialize selectedTeam as empty object
  }),
  actions: {
    async initializeStore(): Promise<void> {
        const storedTeam = localStorage.getItem(CURRENT_TEAM_STORAGE_KEY);
        if (storedTeam) {
          this.selectedTeam = JSON.parse(storedTeam);
        }
    },

    async fetchTeams(): Promise<void> {
      try {
        const response: any = await TeamService.getTeams();
        this.teams = response.results;
        if(!this.$state.selectedTeam.id ) {
          this.setTeamStorage(response.results[0]);
        }
      } catch (error) {
        console.error('Failed to fetch teams', error);
      }
    },

    async createTeam(name: string): Promise<void> {
      try {
        await TeamService.createTeam(name);
        this.fetchTeams();
      } catch (error) {
        console.error('Failed to create team', error);
      }
    },

    async changeCurrentTeam(teamId: string): Promise<void> {
      const currentTeam = this.teams.find((item: any) => item?.id === teamId);
      if (currentTeam) {
        this.setTeamStorage(currentTeam);
      }
    },

    setTeamStorage(currentTeam: any): void {
      const teamId = currentTeam?.id;
      const teamType = currentTeam?.type;
      const teamRole = getCurrentTeamRole(currentTeam);
      this.$state.selectedTeam  = { id: teamId, role: teamRole, type: teamType };
      localStorage.setItem(CURRENT_TEAM_STORAGE_KEY, JSON.stringify(this.selectedTeam));
    },

    resetTeamStorage(): void {
      const defaultTeam = this.teams.find(item =>  item.type === TeamType.PERSONAL)
      this.setTeamStorage(defaultTeam)
    },
  },
});

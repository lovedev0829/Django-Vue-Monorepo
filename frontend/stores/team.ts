import { defineStore } from 'pinia';
import TeamService from "../services/TeamService";
import { CURRENT_TEAM_STORAGE_KEY } from "@/constants/team.global"

export const useTeamStore = defineStore('teams', {
  state: () => ({
    teams: [],
    selectedTeam: null
  }),
  actions: {
    async fetchTeams(): Promise<void> {
      
        try {
            const response =  await TeamService.getTeams();
            this.$state.teams = response.results;
            this.$state.selectedTeam = response.results[0]

        } catch (error) {
            console.error('Failed to fetch teams', error);
        }
    },
    async createTeam(name: string): Promise<void> {
        try {
            await TeamService.createTeam(name);
            this.fetchTeams();
        } catch (error) {
            console.error('Failed to creat teams', error);
        }
    },

    async changeCurrentTeam(teamId: string): Promise<void> {
        this.$state.selectedTeam = this.$state.teams.find( item  =>  item?.id === teamId)
    }
  },
});

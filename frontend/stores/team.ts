import { defineStore } from 'pinia';
import { useAxiosInstance } from '~/api';
import TeamService from "../services/TeamService";

const $axios = useAxiosInstance;

export const useTeamStore = defineStore('teams', {
  state: () => ({
    teams: [], // State to hold team data
  }),
  actions: {

    async fetchTeams(): Promise<void> {
      
        try {
        
            const response =  await TeamService.getTeams();
            this.teams = response.results;

        } catch (error) {
            console.error('Failed to fetch teams', error);
        }
    },

    async createTeam(name: string): Promise<void> {
        try {
            await TeamService.createTeam(name);
            this.fetchTeams();

        } catch (error) {
            console.error('Failed to fetch teams', error);
        }
    }

  },
});

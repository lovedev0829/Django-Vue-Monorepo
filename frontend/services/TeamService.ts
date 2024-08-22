import { useAxiosInstance } from '~/api';
import { TEAM_API_PATH } from '~/constants/apiPath';

const $axios =  useAxiosInstance

export default {

    getTeams() {
        return $axios().get(TEAM_API_PATH.list);
    },
    getTeamByID(teamId: string) {
        return $axios().get(`${TEAM_API_PATH.retrieve}/${teamId}`);
    },
    createTeam(name: string) {
        return $axios().post(TEAM_API_PATH.create, { name: name });
    },

    updateTeam(id: string, name: string) {
        return $axios().put(`${TEAM_API_PATH.update}/${id}`, { name });
    },

    deleteTeam(id: string) {
        return $axios().delete(`${TEAM_API_PATH.destroy}/${id}`);
    },
  
};
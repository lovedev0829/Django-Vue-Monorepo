import { useAxiosInstance } from '~/api';
import { TEAM_API_PATH } from '~/constants/apiPath';

const $axios =  useAxiosInstance

export default {

    getTeams() {
        return $axios().get(TEAM_API_PATH.list);
    },
    createTeam(name: string) {
        return $axios().post(TEAM_API_PATH.create, { name: name });
    },

    updateTeam(name: string) {
        return $axios().post(TEAM_API_PATH.create, { name: name });
    },

    deleteTeam(name: string) {
        return $axios().post(TEAM_API_PATH.create, { name: name });
    },
  
};
import { useAxiosInstance } from '~/api';
import { TEAM_API_PATH } from '~/constants/apiPath';

const $axios =  useAxiosInstance

export default {
    createTeam(name: string) {
        return $axios().post(TEAM_API_PATH.create, { name: name });
    },
  
};
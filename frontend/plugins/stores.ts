import { useUserStore } from "~/stores/user";
import { useTeamStore } from "~/stores/team";

export default defineNuxtPlugin(() => {
    
    const userStore = useUserStore();
    const teamStore = useTeamStore();

    userStore.initializeStore();
    teamStore.initializeStore();

    return {
        provide: {
            userStore,
            teamStore
        },
    };
});
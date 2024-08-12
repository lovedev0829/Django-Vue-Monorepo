import { useUserStore } from "~/stores/user";

export default defineNuxtPlugin(() => {
    
    const userStore = useUserStore();

    userStore.initializeStore();

    return {
        provide: {
            userStore,
        },
        
    };
});
// middleware/auth.global.ts
export default defineNuxtRouteMiddleware((to, from) => {
    const { $userStore } = useNuxtApp();
  
    if ($userStore.isAuthenticated === false && to.path !== '/login' && to.path !== '/signup') {
      return navigateTo('/login');
    } else if ((to.path === '/login' || to.path === '/signup') && $userStore.isAuthenticated === true) {
      return navigateTo('/dashboard');
    }
  });
  
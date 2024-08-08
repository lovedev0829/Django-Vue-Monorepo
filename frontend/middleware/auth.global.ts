// middleware/auth.global.ts
export default defineNuxtRouteMiddleware((to, from) => {
  const { $userStore } = useNuxtApp();
  const router = useRouter();

  if ($userStore.isAuthenticated == false) {
     router.push('/login');
} else if ((
        to.path === '/login' || 
        to.path === '/signup') && 
        $userStore.isAuthenticated == true ) {

     router.push('/dashboard');
  }
});
import { defineStore } from 'pinia';
import { useAxiosInstance } from '~/api';
import { USER_API_PATH } from '~/constants/apiPath';

const $axios =  useAxiosInstance

interface IUser {
    id: string;
    first_name: string;
    last_name: string;
    email: string;
    role: string;
}

interface IUserStoreState {
    user: IUser | null;
    access_token: string;
    refresh_token: string;
    isAuthenticated: string | boolean;
}

interface LoginResponse {
    access_token: string;
    refresh_token: string;
    user: IUser;
}


export const useUserStore = defineStore('user', {
    state: (): IUserStoreState => ({
        user: null,
        access_token: '',
        refresh_token: '',
        isAuthenticated: false,
    }),
    actions: {
        initializeStore() {
            
            const accessToken = useCookie('access_token');
            const refreshToken = useCookie('refresh_token');
            const isAuthenticated = useCookie<string | boolean>('isAuthenticated');
            const userCookie =  useCookie<IUser | null>('user');
            
            this.user = userCookie.value || null;
            this.access_token = accessToken.value || "";
            this.refresh_token = refreshToken.value || "";
            this.isAuthenticated = isAuthenticated.value || false;
        },
        async login(email: string, password: string): Promise<any> {
            
            const response: LoginResponse = await $axios().post(USER_API_PATH.login, {
                email: email,
                password: password
            });

                if(response?.access_token) {
                    this.setTokens(response)
                }

            return response
            
        },

        async register( { firstName, lastName, email, password } : { 
                            firstName: string, 
                            lastName: string, 
                            email: string, 
                            password: string
                        }): Promise<void> {
            
            await $axios().post(USER_API_PATH.register, {
                first_name: firstName,
                last_name: lastName,
                email: email,
                password: password
            })
        },

   
        async logout(): Promise<void> {
            await $axios().post(USER_API_PATH.logout)
            this.resetUser()
        },

        resetUser(): void {
            const accessToken = useCookie('access_token');
            const refreshToken = useCookie('refresh_token');
            const userCookie = useCookie('user');
            const isAuthenticated = useCookie<string | boolean>('isAuthenticated');

            this.$state.access_token = '';
            this.$state.refresh_token = '';
            this.$state.user = null;
            this.$state.isAuthenticated = false;

            accessToken.value = '';
            refreshToken.value = '';
            userCookie.value = null;
            isAuthenticated.value = false;
        },

        setTokens(response: LoginResponse): void {
            const accessToken = useCookie('access_token');
            const refreshToken = useCookie('refresh_token');
            const userCookie = useCookie('user');
            const isAuthenticated = useCookie<string | boolean>('isAuthenticated');

            this.$state.access_token = response.access_token;
            this.$state.refresh_token = response.refresh_token;
            this.$state.user = response.user;
            this.$state.isAuthenticated = true;

            accessToken.value = response.access_token;
            refreshToken.value = response.refresh_token;
            userCookie.value = JSON.stringify(response.user);
            isAuthenticated.value = true;
        },

        async handleGoogleOAuthCallback(code: string): Promise<void> {
            try {
                const response = await $axios().post<LoginResponse>(USER_API_PATH.googleCallback, {
                    code,
                    redirect_uri: 'YOUR_FRONTEND_REDIRECT_URI',
                });
                this.setTokens(response.data);
            } catch (error) {
                throw new Error('Google OAuth Callback Failed');
            }
        }
    },
})

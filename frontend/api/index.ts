import axios from 'axios';
import { USER_API_PATH } from '~/constants/apiPath';

export const useAxiosInstance = () => {
	const config = useRuntimeConfig();
	const refreshToken = useCookie('refresh_token');
	const accessToken = useCookie('access_token');
	const { API_BASE_URL } = config.public;

	const axiosClient = axios.create({
		baseURL: API_BASE_URL,
		headers: {
			'Content-Type': 'application/json',
			Accept: 'application/json',
		},
		withCredentials: false,
	});

	const parseParams = (params: Record<string, any>): string => {
		return Object.entries(params)
			.map(([key, value]) => Array.isArray(value) ? `${key}=${value.join(',')}` : `${key}=${value}`)
			.join('&');
	};

	axiosClient.interceptors.request.use(
		async (config) => {
			if (accessToken?.value) {
				config.headers.Authorization = `Bearer ${accessToken.value}`;
			}
			if (config.method === 'get') {
				config.paramsSerializer = params => parseParams(params);
			}
			return config;
		},
		async (error) => Promise.reject(error)
	);

	axiosClient.interceptors.response.use(
		(response) => {
			if (response === undefined) return;
			return response.data;
		},
		async (error) => {
			const originalRequest = error?.config;

			if (( error.response?.status === 401 || error.response.status === 461 || error.response.status === 403 ) && !originalRequest._retry) {
				originalRequest._retry = true;

				const configHeaders = {
					headers: {
						'Content-Type': 'application/json',
					},
				};
				try {
					const res = await axios.post(
						`${API_BASE_URL}${USER_API_PATH.refresh}`,
						{ refresh: refreshToken.value },
						configHeaders
					);

					if (res.data.access) {
						accessToken.value = res.data.access;
						refreshToken.value = res.data.access;
						originalRequest.headers.Authorization = `Bearer ${res.data.access}`;

						return axiosClient.request(originalRequest);
					}

				} catch (error) {
					return Promise.reject(error);
				}
			}

			return Promise.reject(error);
		}
	);

	return axiosClient;
};

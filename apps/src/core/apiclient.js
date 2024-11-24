import axios from 'axios';
import { Config } from '../config/config';
const useApiClient = () => {
  const defaultOptions = {
    baseURL: `${Config.apiEndpointUrl}`,
    method: ['get', 'post', 'put', 'delete'],
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const axiosInstance = axios.create(defaultOptions);
  axiosInstance.interceptors.request.use(
    (config) => {      
      if (config.data instanceof FormData) {
        config.headers['Content-Type'] = 'multipart/form-data';
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
  return axiosInstance;
};
export default useApiClient;
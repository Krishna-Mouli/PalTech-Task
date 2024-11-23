import axios from 'axios';
import config from '../config/config';

const apiClient = axios.create({
    baseURL: config.apiUrl, 
    headers: {
      'Content-Type': 'application/json',
    },
  });

  const get = async (url, params = {}) => {
    try {
      const response = await apiClient.get(url, { params });
      return response.data;
    } catch (error) {
      console.error('GET request failed:', error);
      throw error;
    }
  };

  const post = async (url, data) => {
    try {
      const response = await apiClient.post(url, data);
      return response.data;
    } catch (error) {
      console.error('POST request failed:', error);
      throw error;
    }
  };

  const put = async (url, data) => {
    try {
      const response = await apiClient.put(url, data);
      return response.data;
    } catch (error) {
      console.error('PUT request failed:', error);
      throw error;
    }
  };

  const del = async (url) => {
    try {
      const response = await apiClient.delete(url);
      return response.data;
    } catch (error) {
      console.error('DELETE request failed:', error);
      throw error;
    }
  };
    
  export default {
    get,
    post,
    put,
    delete: del,
  };
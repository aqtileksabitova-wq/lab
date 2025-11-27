import axios from "axios";
import useAuthStore from "../store/auth";

const api = axios.create({
  baseURL: "https://suzie-undefalcated-carson.ngrok-free.dev",
  withCredentials: false,
  timeout: 30000,
});

api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().token;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;

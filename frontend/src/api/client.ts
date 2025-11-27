import axios from "axios";
import useAuthStore from "../store/auth";

// Используем ngrok URL по умолчанию для работы с Vercel
// Можно переопределить через переменную окружения VITE_API_URL
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? "https://suzie-undefalcated-carson.ngrok-free.dev",
  withCredentials: false,
  timeout: 30000,
});

// Настраиваем interceptors для запросов
api.interceptors.request.use((config) => {
  // Добавляем заголовок для обхода ngrok warning page
  if (config.baseURL?.includes("ngrok-free.dev")) {
    config.headers["ngrok-skip-browser-warning"] = "true";
  }
  
  // Добавляем токен авторизации, если он есть
  const token = useAuthStore.getState().token;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  
  return config;
});

export default api;

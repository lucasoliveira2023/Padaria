import axios from "axios";
import { refreshAccessToken } from "./authServices";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/padaria/usuarios/";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  }
});


api.interceptors.request.use(config => {
  const token = localStorage.getItem("access_token");
  if (token && !config.url?.includes("login") && !config.url?.includes("registro")) {
    config.headers["Authorization"] = `Bearer ${token}`;
  }
  return config;
})



api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;

    if (
      error.response?.status === 401 &&
      !originalRequest._retry &&
      !originalRequest.url.includes("login")
    ) {
      originalRequest._retry = true;
      const newToken = await refreshAccessToken();
      if (newToken) {
        originalRequest.headers["Authorization"] = `Bearer ${newToken}`;
        return api(originalRequest);
      }
    }

    return Promise.reject(error);
  }
);

export default api;

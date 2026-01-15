import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});


api.interceptors.request.use(config =>{
  const token = localStorage.getItem("access_token");
  if (token && !config.url?.includes("login") && !config.url?.includes("refresh")) {
    config.headers["Authorization"] = `Bearer ${token}`;
  }
  return config;
});


api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry && !originalRequest.url.includes("login")) {
      originalRequest._retry = true;

      const refresh = localStorage.getItem("refresh_token");
      if (refresh) {
        try{
          const res = await api.post("/padaria/token/refresh/", {refresh});
          const newAccess = res.data.access;
          localStorage.setItem("access_token", newAccess);
          originalRequest.headers["Authorization"] = `Bearer ${newAccess}`;
          return api(originalRequest);
        } catch (err) {
          console.error("Erro ao atualizar token:", err);
          localStorage.removeItem("access_token");
          localStorage.removeItem("refresh_token");
        }
      }
    }
    return Promise.reject(error);
  }
);


export default api;
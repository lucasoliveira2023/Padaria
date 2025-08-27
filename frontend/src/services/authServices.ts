import api from './api';
import axios from 'axios';


const loginApi = axios.create({
    baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000/padaria/usuarios/",
    headers: { "Content-Type": "application/json"},
});

export const login = async (username: string, password:string) => {
    const response = await loginApi.post("login/", {username, password});

    localStorage.setItem("access_token", response.data.access);
    localStorage.setItem("refresh_token", response.data.refresh);

    return response.data;
};

interface RegisterData {
    username: string;
    password: string;
    nome_completo: string;
    email: string;
    cpf: string;
}


export const registerUser = async (data: RegisterData) => {
    const response = await api.post("registro/", data);
    return response.data;
};


export const refreshAccessToken = async (): Promise<string | null> => {
    const refresh = localStorage.getItem("refresh");
    if (!refresh) return null;

    try {
        const response = await api.post("token/refresh/", { refresh });
        const newAccess = response.data.access;
        localStorage.setItem("token", newAccess);
        return newAccess;
    } catch (error) {
        console.error("Error ao remover token:", error);
        return null;
    }
}
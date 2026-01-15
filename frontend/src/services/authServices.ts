import api from "./api";


export const login = async (username: string, password:string) => {
    const response = await api.post("/padaria/usuarios/login/", {
        username,
        password 
    });

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
    const response = await api.post("/psadaria/usuarios/registro/", data);
    return response.data;
}
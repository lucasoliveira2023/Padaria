import axios from 'axios';

export const login = async (email: string, senha: string) => {
    const response = await axios.post('/padaria/usuarios/login/', {
        email,
        senha,
    });

    return response.data;
};
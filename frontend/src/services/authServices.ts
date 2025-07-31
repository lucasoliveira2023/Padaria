import axios from 'axios';

export const login = async (username: string, password: string) => {
    const response = await axios.post('/padaria/usuarios/login/', {
        username,
        password,
    });

    return response.data;
};
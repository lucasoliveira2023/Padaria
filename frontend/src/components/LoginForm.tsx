import React, { useState } from 'react';
import '../pages/Login.css';
import api from "../services/api";

interface LoginFormProps {
    onLogin:(email: string, password: string) => void;
}

export const LoginForm: React.FC<LoginFormProps> = ({ onLogin }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onLogin(email, password);
    };

    return (
        <form onSubmit={handleSubmit} className="login-form">
            <h2>Login</h2>
            <input
                type="email"
                placeholder="E-mail"
                value={email}
                onChange={e => setEmail(e.target.value)}
                required
            />
            <input
                type="password"
                placeholder="Senha"
                value={password}
                onChange={e => setPassword(e.target.value)}
                required
            />
            <button type="submit">Entrar</button>
        </form>
    );
};

export default LoginForm;
import React, { useState } from 'react';
import '../pages/Login.css';


type LoginFormProps = {
    onLogin: (username: string, password: string) => Promise<void> | void;
};

const LoginForm: React.FC<LoginFormProps> = ({ onLogin }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [erro, setErro] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setErro('');
        try {
            await onLogin(username, password);
        } catch {
            setErro("username ou senha inválidos");
        }
    };

    return (
        <form onSubmit={handleSubmit} className="login-form">
            <input
                type="text"
                name="username"
                autoComplete="off"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Login"
                required
            />
            <input
                type="text"
                name="password"
                autoComplete="off"
                value={password}
                onChange={e => setPassword(e.target.value)}
                placeholder="Senha"
                required
            />
            <button type="submit">Entrar</button>
            {erro && <p style={{ color: "red"}}>{erro}</p>}
        </form>
    );
};

export default LoginForm;
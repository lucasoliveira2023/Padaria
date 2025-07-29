import React, { useState } from 'react';
import '../pages/Login.css';


type LoginFormProps = {
    onLogin: (email: string, senha: string) => Promise<void> | void;
};

const LoginForm: React.FC<LoginFormProps> = ({ onLogin }) => {
    const [email, setEmail] = useState("");
    const [senha, setSenha] = useState("");
    const [erro, setErro] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setErro('');
        try {
            await onLogin(email, senha);
        } catch (err: any) {
            setErro("E-mail ou senha inválidos");
        }
    };

    return (
        <form onSubmit={handleSubmit} className="login-form">
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="E-mail"
                required
            />
            <input
                type="password"
                value={senha}
                onChange={e => setSenha(e.target.value)}
                placeholder="Senha"
                required
            />
            <button type="submit">Entrar</button>
            {erro && <p style={{ color: "red"}}>{erro}</p>}
        </form>
    );
};

export default LoginForm;
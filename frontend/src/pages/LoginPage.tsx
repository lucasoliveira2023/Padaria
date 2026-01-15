// src/pages/LoginPage.tsx
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../services/authServices";
import "../pages/Login.css";

const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    try {
      await login(username, password);
      alert("Login realizado com sucesso!");
      navigate("/"); // redireciona para a home
    } catch (err) {
      console.error(err);
      setError("Falha no login. Verifique suas credenciais.");
    }
  };

  return (
    <div className="register-page-wrapper">
      <div className="register-container">
        <form onSubmit={handleLogin} className="register-form">
          <h1>Login</h1>

          <input
            type="text"
            placeholder="Usuário"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />

          <input
            type="password"
            placeholder="Senha"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button type="submit">Entrar</button>

          {error && <p className="error">{error}</p>}
        </form>
      </div>
    </div>
  );
};

export default LoginPage;

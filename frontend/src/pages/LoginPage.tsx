// src/pages/LoginPage.tsx
import React from 'react';
import LoginForm from '../components/LoginForm';
import { login } from '../services/authServices';

const LoginPage: React.FC = () => {
  const handleLogin = async (email: string, senha: string) => {
    try {
      const response = await login(email, senha);
      alert('Login realizado com sucesso!');
      console.log(response);
      // aqui pode salvar token, redirecionar, etc
    } catch (error) {
      alert('Falha no login. Verifique suas credenciais.');
      console.error(error);
    }
  };

  return (
    <div className="login-page">
      <LoginForm onLogin={handleLogin} />
    </div>
  );
};

export default LoginPage;

// src/pages/LoginPage.tsx
import React from 'react';
import LoginForm from '../components/LoginForm';
import { login } from '../services/authServices';

const LoginPage: React.FC = () => {
  const handleLogin = async (username: string, password: string) => {
    try{
      const response = await login(username, password);
      alert('Login realizado com sucesso!');
      console.log(response);
    } catch (error) {
      alert('Falha no login. Verifique suas credenciais.');
      console.error(error);
    }
  }

  return (
    <div className="login-page">
      <LoginForm onLogin={handleLogin} />
    </div>
  );
};

export default LoginPage;

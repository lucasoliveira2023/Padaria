// src/pages/LoginPage.tsx
import React from 'react';
import { LoginForm } from '../components/LoginForm';
import { login } from '../services/authServices';


export const LoginPage: React.FC = () => {
  const handleLogin = async(email: string, password: string) => {
    try{
      const response = await login(email, password);
      alert('Login realizado com sucesso!');
      console.log(response);
      // redirecionar, salvar token, etc, ver a api e decidir
    } catch (error) {
      alert('Falha no login. Verifique suas credenciais.');
    }
  };


  return (
    <div className="login-page">
      <LoginForm onLogin={handleLogin}/>
    </div>
  );
};
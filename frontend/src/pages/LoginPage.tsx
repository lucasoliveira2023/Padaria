// src/pages/LoginPage.tsx
import React from 'react';
import LoginForm from '../components/LoginForm';
import { useAuth } from '../hooks/useAuth';

const LoginPage: React.FC = () => {
  const { signIn } = useAuth();

  const handleLogin = async (username: string, password:string) =>{
    const success = await signIn(username, password);
    if (success) {
      alert('Login realizado com sucesso!');
    } else {
      alert('Falha no login. Verifique suas credenciais.');
    }
  };

  return (
    <div className='login-page'>
      <LoginForm onLogin={handleLogin} />
    </div>
  );
};
export default LoginPage;

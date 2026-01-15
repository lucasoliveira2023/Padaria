// src/pages/UserProfile.tsx
import React, { useEffect, useState } from "react";
import api from "../services/api";

interface Profile {
  id: number;
  username: string;
  email: string;
  nome_completo: string;
  cpf: string;
  telefone?: string;
  tipo_usuario?: string;
}

const UserProfile: React.FC = () => {
  const [user, setUser] = useState<Profile | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const res = await api.get("/padaria/usuarios/profile/");
        setUser(res.data);
      } catch (err) {
        console.error(err);
        setError("Erro ao carregar perfil do usuário.");
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, []);

  if (loading) return <p>Carregando...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div className="register-page-wrapper">
      <div className="register-container">
        <h1>Perfil do Usuário</h1>
        {user && (
          <div className="register-form">
            <p><strong>Username:</strong> {user.username}</p>
            <p><strong>Email:</strong> {user.email}</p>
            <p><strong>Nome Completo:</strong> {user.nome_completo}</p>
            <p><strong>CPF:</strong> {user.cpf}</p>
            {user.telefone && <p><strong>Telefone:</strong> {user.telefone}</p>}
            {user.tipo_usuario && <p><strong>Tipo de Usuário:</strong> {user.tipo_usuario}</p>}
          </div>
        )}
      </div>
    </div>
  );
};

export default UserProfile;

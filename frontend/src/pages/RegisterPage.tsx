import React, { useState } from "react";
import { registerUser } from "../services/authServices";
import "./RegisterPage.css";

const RegisterPage: React.FC = () => {
  const [form, setForm] = useState({
    username: "",
    password: "",
    nome_completo: "",
    email: "",
    cpf: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setSuccess(false);

    try {
      await registerUser(form);

      setSuccess(true);
      setForm({
        username: "",
        password: "",
        nome_completo: "",
        email: "",
        cpf: "",
      });
    } catch (err: unknown) {
      if (err && typeof err === "object" && "response" in err) {
        const axiosError = err as { response?: { data?: { message?: string } } };
        setError(axiosError.response?.data?.message || "Erro ao registrar usuário");
      } else if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Erro ao registrar usuário");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="register-page-wrapper">
      <div className="register-container">
        <form onSubmit={handleSubmit} className="register-form">
          <h1>Registro de Usuário</h1>

          <input
            type="text"
            name="username"
            placeholder="Usuário"
            value={form.username}
            onChange={handleChange}
            required
          />

          <input
            type="password"
            name="password"
            placeholder="Senha"
            value={form.password}
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="nome_completo"
            placeholder="Nome Completo"
            value={form.nome_completo}
            onChange={handleChange}
            required
          />

          <input
            type="email"
            name="email"
            placeholder="E-mail"
            value={form.email}
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="cpf"
            placeholder="CPF"
            value={form.cpf}
            onChange={handleChange}
            required
          />

          <button type="submit" disabled={loading}>
            {loading ? "Registrando..." : "Registrar"}
          </button>

          {error && <p className="error">{error}</p>}
          {success && <p className="success">Usuário registrado com sucesso! Agora faça o login.</p>}
        </form>
      </div>
    </div>
  );
};

export default RegisterPage;

import React, { useState } from "react";
import { registerUser } from "../services/authServices";

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
      // Tratamento seguro do erro
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
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-6 rounded-2xl shadow-md w-96 space-y-4"
      >
        <h1 className="text-xl font-bold text-center text-gray-700">
          Registro de Usuário
        </h1>

        <input
          type="text"
          name="username"
          placeholder="Usuário"
          value={form.username}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Senha"
          value={form.password}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />

        <input
          type="text"
          name="nome_completo"
          placeholder="Nome Completo"
          value={form.nome_completo}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />

        <input
          type="email"
          name="email"
          placeholder="E-mail"
          value={form.email}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />

        <input
          type="text"
          name="cpf"
          placeholder="CPF"
          value={form.cpf}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600 transition"
        >
          {loading ? "Registrando..." : "Registrar"}
        </button>

        {error && <p className="text-red-500 text-sm">{error}</p>}
        {success && (
          <p className="text-green-500 text-sm">
            Usuário registrado com sucesso! Agora faça o login.
          </p>
        )}
      </form>
    </div>
  );
};

export default RegisterPage;

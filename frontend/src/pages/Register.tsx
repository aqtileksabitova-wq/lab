import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { register, login, fetchProfile } from "../api/auth";
import useAuthStore from "../store/auth";

const Register = () => {
  const navigate = useNavigate();
  const { setAuth, setToken } = useAuthStore();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      await register(email, password);
      const tokenResponse = await login(email, password);
      setToken(tokenResponse.access_token);
      const profile = await fetchProfile();
      setAuth(tokenResponse.access_token, profile);
      navigate("/dashboard");
    } catch {
      setError("Не удалось создать аккаунт");
    }
  };

  return (
    <div className="mx-auto max-w-md rounded-2xl border border-slate-200 bg-white p-6">
      <h1 className="text-2xl font-bold text-slate-900">Регистрация</h1>
      <form onSubmit={handleSubmit} className="mt-6 space-y-4">
        <input
          type="email"
          placeholder="Email"
          className="w-full rounded-lg border border-slate-200 p-3"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Пароль"
          className="w-full rounded-lg border border-slate-200 p-3"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button className="w-full rounded-lg bg-indigo-600 py-3 text-white">Создать аккаунт</button>
        {error && <p className="text-sm text-red-600">{error}</p>}
      </form>
      <p className="mt-4 text-sm text-slate-600">
        Уже есть аккаунт?{" "}
        <Link to="/login" className="text-indigo-600">
          Войти
        </Link>
      </p>
    </div>
  );
};

export default Register;


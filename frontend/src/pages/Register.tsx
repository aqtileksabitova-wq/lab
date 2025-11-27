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
    <div className="mx-auto max-w-md">
      <div className="rounded-2xl border-2 border-slate-200 bg-white p-8 shadow-xl">
        <div className="mb-8 text-center">
          <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-gradient-to-br from-indigo-500 to-purple-500 text-3xl text-white">
            ✨
          </div>
          <h1 className="text-3xl font-bold text-slate-900">Создать аккаунт</h1>
          <p className="mt-2 text-slate-600">Начните свой путь в изучении C++</p>
        </div>
        <form onSubmit={handleSubmit} className="space-y-5">
          <div>
            <label className="mb-2 block text-sm font-semibold text-slate-700">Email</label>
            <input
              type="email"
              placeholder="your@email.com"
              className="w-full rounded-lg border-2 border-slate-200 bg-slate-50 px-4 py-3 transition-all focus:border-indigo-500 focus:bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500/20"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div>
            <label className="mb-2 block text-sm font-semibold text-slate-700">Пароль</label>
            <input
              type="password"
              placeholder="••••••••"
              className="w-full rounded-lg border-2 border-slate-200 bg-slate-50 px-4 py-3 transition-all focus:border-indigo-500 focus:bg-white focus:outline-none focus:ring-2 focus:ring-indigo-500/20"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          {error && (
            <div className="rounded-lg border border-red-200 bg-red-50 p-3">
              <p className="text-sm font-medium text-red-600">{error}</p>
            </div>
          )}
          <button
            type="submit"
            className="w-full rounded-lg bg-gradient-to-r from-indigo-600 to-purple-600 py-3 font-semibold text-white shadow-lg transition-all hover:scale-[1.02] hover:shadow-xl"
          >
            Создать аккаунт
          </button>
        </form>
        <p className="mt-6 text-center text-sm text-slate-600">
          Уже есть аккаунт?{" "}
          <Link to="/login" className="font-semibold text-indigo-600 hover:text-indigo-500">
            Войти
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Register;


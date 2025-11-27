import type { ReactNode } from "react";
import { Link, NavLink } from "react-router-dom";
import useAuthStore from "../store/auth";

const navItems = [
  { label: "Лекции", to: "/lectures" },
  { label: "Видео", to: "/videos" },
  { label: "Компилятор", to: "/compiler" },
  { label: "Кабинет", to: "/dashboard" },
  { label: "Админ", to: "/admin", requiresAdmin: true },
];

const Layout = ({ children }: { children: ReactNode }) => {
  const { user, logout } = useAuthStore();

  return (
    <div className="min-h-screen bg-slate-50">
      <header className="border-b border-slate-200 bg-white shadow-sm">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4">
          <Link
            to="/"
            className="flex items-center gap-2 text-2xl font-bold text-indigo-600 transition-all hover:scale-105"
          >
            <span className="text-3xl">⚡</span>
            <span>CppLearn</span>
          </Link>
          <nav className="flex items-center gap-2 text-sm font-medium">
            {navItems
              .filter((item) => !item.requiresAdmin || user?.role === "admin")
              .map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  className={({ isActive }) =>
                    `rounded-lg px-4 py-2 transition-all ${
                      isActive
                        ? "bg-indigo-100 font-semibold text-indigo-600"
                        : "text-slate-600 hover:bg-slate-100 hover:text-indigo-600"
                    }`
                  }
                >
                  {item.label}
                </NavLink>
              ))}
          </nav>
          <div className="flex items-center gap-3">
            {user ? (
              <>
                <div className="flex items-center gap-2 rounded-lg bg-slate-100 px-3 py-2">
                  <span className="text-sm font-medium text-slate-700">{user.email}</span>
                  {user.role === "admin" && (
                    <span className="rounded-full bg-indigo-100 px-2 py-0.5 text-xs font-semibold text-indigo-600">
                      Admin
                    </span>
                  )}
                </div>
                <button
                  onClick={logout}
                  className="rounded-lg border-2 border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-600 transition-all hover:border-red-300 hover:bg-red-50 hover:text-red-600"
                >
                  Выйти
                </button>
              </>
            ) : (
              <>
                <Link
                  to="/login"
                  className="rounded-lg px-4 py-2 text-sm font-medium text-slate-600 transition-all hover:text-indigo-600"
                >
                  Вход
                </Link>
                <Link
                  to="/register"
                  className="rounded-lg bg-gradient-to-r from-indigo-600 to-purple-600 px-4 py-2 text-sm font-semibold text-white shadow-md transition-all hover:scale-105 hover:shadow-lg"
                >
                  Регистрация
                </Link>
              </>
            )}
          </div>
        </div>
      </header>
      <main className="mx-auto max-w-6xl px-4 py-8">{children}</main>
    </div>
  );
};

export default Layout;


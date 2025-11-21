import type { ReactNode } from "react";
import { Link, NavLink } from "react-router-dom";
import useAuthStore from "../store/auth";

const navItems = [
  { label: "Лекции", to: "/lectures" },
  { label: "Кабинет", to: "/dashboard" },
  { label: "Админ", to: "/admin" },
];

const Layout = ({ children }: { children: ReactNode }) => {
  const { user, logout } = useAuthStore();

  return (
    <div className="min-h-screen bg-slate-50">
      <header className="bg-white shadow-sm">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4">
          <Link to="/" className="text-xl font-semibold text-indigo-600">
            CppLearn
          </Link>
          <nav className="flex items-center gap-4 text-sm font-medium text-slate-600">
            {navItems
              .filter((item) => item.to !== "/admin" || user?.role === "admin")
              .map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive }) =>
                  isActive ? "text-indigo-600" : "hover:text-indigo-500"
                }
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
          <div className="flex items-center gap-3">
            {user ? (
              <>
                <span className="text-sm text-slate-600">{user.email}</span>
                <button
                  onClick={logout}
                  className="rounded-md border border-slate-200 px-3 py-1 text-sm text-slate-600 hover:bg-slate-100"
                >
                  Выйти
                </button>
              </>
            ) : (
              <>
                <Link to="/login" className="text-sm text-slate-600 hover:text-indigo-600">
                  Вход
                </Link>
                <Link
                  to="/register"
                  className="rounded-md bg-indigo-600 px-3 py-1 text-sm text-white hover:bg-indigo-500"
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


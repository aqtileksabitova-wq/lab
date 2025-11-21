import { Navigate } from "react-router-dom";
import useAuthStore from "../store/auth";

const ProtectedRoute = ({ children, requireAdmin = false }: { children: JSX.Element; requireAdmin?: boolean }) => {
  const { token, user } = useAuthStore();
  if (!token) {
    return <Navigate to="/login" replace />;
  }
  if (requireAdmin) {
    if (!user) {
      return <p className="p-4">Проверка прав...</p>;
    }
    if (user.role !== "admin") {
      return <Navigate to="/" replace />;
    }
  }
  return children;
};

export default ProtectedRoute;


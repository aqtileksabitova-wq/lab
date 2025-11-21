import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useAuthStore from "../store/auth";
import { fetchProfile } from "../api/auth";

export const useAuthGuard = (requireAdmin = false) => {
  const { token, user, setUser, logout } = useAuthStore();
  const navigate = useNavigate();

  useEffect(() => {
    const ensureProfile = async () => {
      if (!token) {
        navigate("/login");
        return;
      }
      if (!user) {
        try {
          const profile = await fetchProfile();
          setUser(profile);
        } catch {
          logout();
          navigate("/login");
        }
      } else if (requireAdmin && user.role !== "admin") {
        navigate("/");
      }
    };
    ensureProfile();
  }, [token, user, setUser, logout, navigate, requireAdmin]);

  return { user, token };
};


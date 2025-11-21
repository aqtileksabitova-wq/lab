import api from "./client";
import type { User } from "../types";

interface AuthResponse {
  access_token: string;
  token_type: string;
}

export const login = async (email: string, password: string) => {
  const params = new URLSearchParams();
  params.append("username", email);
  params.append("password", password);
  const { data } = await api.post<AuthResponse>("/auth/login", params);
  return data;
};

export const register = async (email: string, password: string) => {
  const { data } = await api.post<User>("/auth/register", { email, password });
  return data;
};

export const fetchProfile = async () => {
  const { data } = await api.get<User>("/auth/me");
  return data;
};


import api from "./client";
import type { CompileResponse } from "../types";

export interface CompileRequest {
  source: string;
  std?: "c++17" | "c++20";
}

export const runCompiler = async (payload: CompileRequest) => {
  const { data } = await api.post<CompileResponse>("/compiler/run", payload);
  return data;
};




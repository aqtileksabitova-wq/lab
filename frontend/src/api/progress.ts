import api from "./client";
import type { Progress, TestResult } from "../types";

export const fetchProgress = async () => {
  const { data } = await api.get<Progress[]>("/users/me/progress");
  return data;
};

export const fetchResults = async () => {
  const { data } = await api.get<TestResult[]>("/users/me/results");
  return data;
};

export const updateProgress = async (progress: Pick<Progress, "lecture_id" | "status">) => {
  const { data } = await api.post<Progress>("/progress/update", progress);
  return data;
};


import api from "./client";
import type { Test, TestResult } from "../types";

interface SubmissionPayload {
  answers: {
    question_id: number;
    selected_answer_ids: number[];
  }[];
}

export const fetchTest = async (id: number) => {
  const { data } = await api.get<Test>(`/tests/${id}`);
  return data;
};

export const submitTest = async (id: number, payload: SubmissionPayload) => {
  const { data } = await api.post<TestResult>(`/tests/${id}/submit`, payload);
  return data;
};

interface TestPayload {
  lecture_id: number;
  title: string;
  description?: string;
  questions: {
    question_text: string;
    question_type: "single" | "multi";
    explanation?: string;
    answers: {
      answer_text: string;
      is_correct: boolean;
    }[];
  }[];
}

export const createTest = async (payload: TestPayload) => {
  const { data } = await api.post<Test>("/tests", payload);
  return data;
};


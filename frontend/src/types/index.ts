export type UserRole = "guest" | "user" | "admin";

export interface User {
  id: number;
  email: string;
  role: UserRole;
  created_at: string;
}

export interface Lecture {
  id: number;
  title: string;
  short_description: string;
  content: string;
  created_at: string;
  updated_at: string;
}

export interface Answer {
  id: number;
  answer_text: string;
  is_correct: boolean;
}

export interface Question {
  id: number;
  question_text: string;
  question_type: "single" | "multi";
  explanation?: string | null;
  answers: Answer[];
}

export interface Test {
  id: number;
  lecture_id: number;
  title: string;
  description?: string | null;
  questions: Question[];
}

export interface Progress {
  user_id: number;
  lecture_id: number;
  status: "not_started" | "in_progress" | "completed";
}

export interface TestResult {
  id: number;
  test_id: number;
  score: number;
  total: number;
  passed_at: string;
}

export interface ApiError {
  detail: string;
}


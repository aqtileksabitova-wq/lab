import api from "./client";
import type { Lecture, Test } from "../types";

export const fetchLectures = async () => {
  const { data } = await api.get<Lecture[]>("/lectures");
  return data;
};

export const fetchLecture = async (id: number) => {
  const { data } = await api.get<Lecture>(`/lectures/${id}`);
  return data;
};

export const fetchLectureTests = async (lectureId: number) => {
  const { data } = await api.get<Test[]>(`/lectures/${lectureId}/tests`);
  return data;
};

interface LecturePayload {
  title: string;
  short_description: string;
  content: string;
}

export const createLecture = async (payload: LecturePayload) => {
  const { data } = await api.post<Lecture>("/lectures", payload);
  return data;
};


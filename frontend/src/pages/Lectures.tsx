import { useEffect, useState } from "react";
import { fetchLectures } from "../api/lectures";
import LectureCard from "../components/LectureCard";
import type { Lecture } from "../types";

const Lectures = () => {
  const [lectures, setLectures] = useState<Lecture[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLectures()
      .then(setLectures)
      .finally(() => setLoading(false));
  }, []);

  if (loading)
    return (
      <div className="flex items-center justify-center py-20">
        <div className="text-center">
          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-indigo-200 border-t-indigo-600"></div>
          <p className="mt-4 text-slate-600">Загрузка лекций...</p>
        </div>
      </div>
    );

  return (
    <section className="space-y-8">
      <div className="rounded-2xl bg-gradient-to-r from-indigo-50 to-purple-50 p-8">
        <h1 className="text-4xl font-bold text-slate-900">Лекции по C++</h1>
        <p className="mt-2 text-lg text-slate-600">
          Изучайте программирование на C++ от основ до продвинутых тем
        </p>
        <div className="mt-4 inline-flex items-center gap-2 rounded-full bg-white px-4 py-2 shadow-sm">
          <span className="text-sm font-semibold text-slate-700">Доступно тем:</span>
          <span className="rounded-full bg-indigo-100 px-3 py-1 text-sm font-bold text-indigo-600">
            {lectures.length}
          </span>
        </div>
      </div>
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {lectures.map((lecture) => (
          <LectureCard key={lecture.id} lecture={lecture} />
        ))}
      </div>
    </section>
  );
};

export default Lectures;


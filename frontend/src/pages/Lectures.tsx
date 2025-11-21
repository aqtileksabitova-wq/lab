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

  if (loading) return <p>Загрузка...</p>;

  return (
    <section className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-slate-900">Лекции</h2>
        <p className="text-sm text-slate-500">3 базовые лекции с автоинициализацией</p>
      </div>
      <div className="grid gap-4 md:grid-cols-2">
        {lectures.map((lecture) => (
          <LectureCard key={lecture.id} lecture={lecture} />
        ))}
      </div>
    </section>
  );
};

export default Lectures;


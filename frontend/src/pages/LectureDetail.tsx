import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { fetchLecture, fetchLectureTests } from "../api/lectures";
import { marked } from "marked";
import type { Lecture, Test } from "../types";

const LectureDetail = () => {
  const { id } = useParams();
  const lectureId = Number(id);
  const [lecture, setLecture] = useState<Lecture | null>(null);
  const [tests, setTests] = useState<Test[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!lectureId) return;
    Promise.all([fetchLecture(lectureId), fetchLectureTests(lectureId)])
      .then(([lectureResponse, testsResponse]) => {
        setLecture(lectureResponse);
        setTests(testsResponse);
      })
      .finally(() => setLoading(false));
  }, [lectureId]);

  if (loading) return <p>Загрузка...</p>;
  if (!lecture) return <p>Лекция не найдена</p>;

  return (
    <article className="space-y-6">
      <header className="space-y-2 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
        <p className="text-sm uppercase text-indigo-600">Лекция #{lecture.id}</p>
        <h1 className="text-3xl font-bold text-slate-900">{lecture.title}</h1>
        <p className="text-slate-600">{lecture.short_description}</p>
      </header>
      <section className="prose max-w-none rounded-2xl border border-slate-200 bg-white p-6">
        <div dangerouslySetInnerHTML={{ __html: marked.parse(lecture.content) }} />
      </section>
      <section className="rounded-2xl border border-slate-200 bg-white p-6">
        <h3 className="text-xl font-semibold text-slate-900">Тесты</h3>
        <div className="mt-4 flex flex-col gap-3">
          {tests.map((test) => (
            <Link
              key={test.id}
              className="rounded-xl border border-indigo-100 bg-indigo-50 px-4 py-3 text-indigo-700"
              to={`/tests/${test.id}`}
            >
              {test.title}
            </Link>
          ))}
        </div>
      </section>
    </article>
  );
};

export default LectureDetail;


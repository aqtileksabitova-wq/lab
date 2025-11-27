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

  if (loading)
    return (
      <div className="flex items-center justify-center py-20">
        <div className="text-center">
          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-indigo-200 border-t-indigo-600"></div>
          <p className="mt-4 text-slate-600">Загрузка лекции...</p>
        </div>
      </div>
    );
  if (!lecture)
    return (
      <div className="rounded-xl border border-red-200 bg-red-50 p-6 text-center">
        <p className="text-red-600">Лекция не найдена</p>
      </div>
    );

  return (
    <article className="space-y-8">
      <header className="space-y-4 rounded-2xl bg-gradient-to-r from-indigo-50 to-purple-50 p-8 shadow-sm">
        <div className="inline-flex items-center gap-2 rounded-full bg-white px-4 py-2 shadow-sm">
          <span className="text-sm font-semibold text-indigo-600">Лекция #{lecture.id}</span>
        </div>
        <h1 className="text-4xl font-bold text-slate-900">{lecture.title}</h1>
        <p className="text-lg leading-relaxed text-slate-600">{lecture.short_description}</p>
      </header>
      <section className="prose prose-slate max-w-none rounded-2xl border-2 border-slate-200 bg-white p-8 shadow-sm prose-headings:font-bold prose-headings:text-slate-900 prose-h1:text-3xl prose-h2:text-2xl prose-h3:text-xl prose-p:text-slate-700 prose-p:leading-relaxed prose-code:rounded prose-code:bg-slate-100 prose-code:px-1.5 prose-code:py-0.5 prose-code:text-sm prose-code:font-mono prose-code:text-indigo-700 prose-pre:bg-slate-900 prose-pre:text-slate-100 prose-strong:text-slate-900 prose-ul:list-disc prose-ol:list-decimal">
        <div dangerouslySetInnerHTML={{ __html: marked.parse(lecture.content) }} />
      </section>
      {tests.length > 0 && (
        <section className="rounded-2xl border-2 border-slate-200 bg-white p-8 shadow-sm">
          <h3 className="mb-6 text-2xl font-bold text-slate-900">Доступные тесты</h3>
          <div className="grid gap-4 md:grid-cols-2">
            {tests.map((test) => (
              <Link
                key={test.id}
                className="group flex items-center justify-between rounded-xl border-2 border-indigo-100 bg-indigo-50 px-6 py-4 transition-all hover:border-indigo-300 hover:bg-indigo-100 hover:shadow-md"
                to={`/tests/${test.id}`}
              >
                <div>
                  <h4 className="font-semibold text-indigo-900">{test.title}</h4>
                  {test.description && (
                    <p className="mt-1 text-sm text-indigo-700">{test.description}</p>
                  )}
                </div>
                <span className="text-xl text-indigo-600 transition-transform group-hover:translate-x-1">
                  →
                </span>
              </Link>
            ))}
          </div>
        </section>
      )}
    </article>
  );
};

export default LectureDetail;


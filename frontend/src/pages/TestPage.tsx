import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchTest, submitTest } from "../api/tests";
import TestQuestion from "../components/TestQuestion";
import type { Question, Test, TestResult } from "../types";
import useAuthStore from "../store/auth";

const TestPage = () => {
  const { id } = useParams();
  const testId = Number(id);
  const [test, setTest] = useState<Test | null>(null);
  const [selected, setSelected] = useState<Record<number, number[]>>({});
  const [result, setResult] = useState<TestResult | null>(null);
  const [loading, setLoading] = useState(true);
  const { token } = useAuthStore();

  useEffect(() => {
    if (!testId || !token) return;
    fetchTest(testId)
      .then((data) => {
        setTest(data);
        const initial = data.questions.reduce<Record<number, number[]>>((acc, q) => {
          acc[q.id] = [];
          return acc;
        }, {});
        setSelected(initial);
      })
      .finally(() => setLoading(false));
  }, [testId, token]);

  const handleSelect = (question: Question, answerId: number) => {
    setSelected((prev) => {
      const current = prev[question.id] ?? [];
      if (question.question_type === "single") {
        return { ...prev, [question.id]: [answerId] };
      }
      const exists = current.includes(answerId);
      return {
        ...prev,
        [question.id]: exists ? current.filter((id) => id !== answerId) : [...current, answerId],
      };
    });
  };

  const handleSubmit = async () => {
    if (!test || !token) return;
    const payload = {
      answers: Object.entries(selected).map(([questionId, answerIds]) => ({
        question_id: Number(questionId),
        selected_answer_ids: answerIds,
      })),
    };
    const data = await submitTest(test.id, payload);
    setResult(data);
  };

  if (!token)
    return (
      <div className="rounded-xl border border-amber-200 bg-amber-50 p-6 text-center">
        <p className="text-amber-800">Авторизуйтесь, чтобы пройти тест.</p>
      </div>
    );
  if (loading)
    return (
      <div className="flex items-center justify-center py-20">
        <div className="text-center">
          <div className="mx-auto h-12 w-12 animate-spin rounded-full border-4 border-indigo-200 border-t-indigo-600"></div>
          <p className="mt-4 text-slate-600">Загрузка теста...</p>
        </div>
      </div>
    );
  if (!test)
    return (
      <div className="rounded-xl border border-red-200 bg-red-50 p-6 text-center">
        <p className="text-red-600">Тест не найден</p>
      </div>
    );

  const answeredCount = Object.values(selected).filter((arr) => arr.length > 0).length;
  const allAnswered = answeredCount === test.questions.length;

  return (
    <section className="space-y-8">
      <header className="rounded-2xl bg-gradient-to-r from-indigo-50 to-purple-50 p-8 shadow-sm">
        <div className="mb-4 inline-flex items-center gap-2 rounded-full bg-white px-4 py-2 shadow-sm">
          <span className="text-sm font-semibold text-indigo-600">Тест #{test.id}</span>
        </div>
        <h1 className="text-4xl font-bold text-slate-900">{test.title}</h1>
        {test.description && <p className="mt-2 text-lg text-slate-600">{test.description}</p>}
        <div className="mt-4 flex items-center gap-4 text-sm text-slate-500">
          <span>Вопросов: {test.questions.length}</span>
          <span>•</span>
          <span className={allAnswered ? "font-semibold text-green-600" : ""}>
            Отвечено: {answeredCount}/{test.questions.length}
          </span>
        </div>
      </header>
      <div className="space-y-6">
        {test.questions.map((question, index) => (
          <div key={question.id} className="relative">
            <div className="absolute -left-4 top-6 flex h-8 w-8 items-center justify-center rounded-full bg-indigo-100 text-sm font-bold text-indigo-600">
              {index + 1}
            </div>
            <TestQuestion
              question={question}
              selected={selected[question.id] ?? []}
              onSelect={(answerId) => handleSelect(question, answerId)}
            />
          </div>
        ))}
      </div>
      <div className="sticky bottom-4 rounded-xl border-2 border-indigo-200 bg-white p-4 shadow-xl">
        <button
          className="w-full rounded-lg bg-gradient-to-r from-indigo-600 to-purple-600 px-6 py-3 font-semibold text-white shadow-lg transition-all hover:scale-[1.02] hover:shadow-xl disabled:opacity-50 disabled:hover:scale-100"
          onClick={handleSubmit}
          disabled={!allAnswered}
        >
          {allAnswered ? "✓ Отправить ответы" : `Ответьте на все вопросы (${test.questions.length - answeredCount} осталось)`}
        </button>
      </div>
      {result && (
        <div className="rounded-2xl border-2 border-green-200 bg-gradient-to-r from-green-50 to-emerald-50 p-8 shadow-lg">
          <div className="text-center">
            <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-green-100 text-3xl">
              {result.score === result.total ? "🎉" : result.score / result.total >= 0.8 ? "👍" : "📝"}
            </div>
            <h3 className="mb-2 text-2xl font-bold text-green-900">Результат теста</h3>
            <p className="text-4xl font-bold text-green-600">
              {result.score} / {result.total}
            </p>
            <p className="mt-2 text-lg text-green-700">
              {Math.round((result.score / result.total) * 100)}% правильных ответов
            </p>
          </div>
        </div>
      )}
    </section>
  );
};

export default TestPage;


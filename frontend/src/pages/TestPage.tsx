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

  if (!token) return <p>Авторизуйтесь, чтобы пройти тест.</p>;
  if (loading) return <p>Загрузка...</p>;
  if (!test) return <p>Тест не найден</p>;

  return (
    <section className="space-y-6">
      <header>
        <p className="text-sm text-indigo-600">Тест #{test.id}</p>
        <h1 className="text-3xl font-bold text-slate-900">{test.title}</h1>
        <p className="text-slate-600">{test.description}</p>
      </header>
      <div className="space-y-4">
        {test.questions.map((question) => (
          <TestQuestion
            key={question.id}
            question={question}
            selected={selected[question.id] ?? []}
            onSelect={(answerId) => handleSelect(question, answerId)}
          />
        ))}
      </div>
      <button
        className="rounded-xl bg-indigo-600 px-5 py-2 text-white hover:bg-indigo-500"
        onClick={handleSubmit}
      >
        Отправить ответы
      </button>
      {result && (
        <div className="rounded-xl border border-green-100 bg-green-50 p-4 text-green-700">
          Вы набрали {result.score} из {result.total}
        </div>
      )}
    </section>
  );
};

export default TestPage;


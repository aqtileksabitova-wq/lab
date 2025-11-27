import { useEffect, useState } from "react";
import { fetchProgress, fetchResults } from "../api/progress";
import type { Progress, TestResult } from "../types";
import ProgressSummary from "../components/ProgressSummary";
import useAuthStore from "../store/auth";
import { Link } from "react-router-dom";

const Dashboard = () => {
  const { token } = useAuthStore();
  const [progress, setProgress] = useState<Progress[]>([]);
  const [results, setResults] = useState<TestResult[]>([]);

  useEffect(() => {
    if (!token) return;
    fetchProgress().then(setProgress);
    fetchResults().then(setResults);
  }, [token]);

  if (!token) {
    return (
      <div className="rounded-2xl border-2 border-slate-200 bg-gradient-to-br from-indigo-50 to-purple-50 p-12 text-center shadow-lg">
        <div className="mx-auto mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-indigo-100 text-4xl">
          👤
        </div>
        <p className="text-xl font-semibold text-slate-700">Авторизуйтесь, чтобы видеть личный кабинет</p>
        <p className="mt-2 text-slate-600">Отслеживайте свой прогресс и историю прохождений</p>
        <Link
          to="/login"
          className="mt-6 inline-block rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 px-6 py-3 font-semibold text-white shadow-lg transition-all hover:scale-105 hover:shadow-xl"
        >
          Перейти ко входу
        </Link>
      </div>
    );
  }

  return (
    <section className="space-y-8">
      <div className="rounded-2xl bg-gradient-to-r from-indigo-50 to-purple-50 p-8">
        <h1 className="text-4xl font-bold text-slate-900">Личный кабинет</h1>
        <p className="mt-2 text-lg text-slate-600">Отслеживайте свой прогресс и результаты тестов</p>
      </div>
      <div className="grid gap-6 md:grid-cols-2">
        <ProgressSummary progress={progress} />
        <div className="rounded-2xl border-2 border-slate-200 bg-white p-6 shadow-lg">
          <div className="mb-6 flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-indigo-100 text-indigo-600">
              📝
            </div>
            <h3 className="text-xl font-bold text-slate-900">История тестов</h3>
          </div>
          <div className="space-y-3">
            {results.map((result) => {
              const percentage = Math.round((result.score / result.total) * 100);
              return (
                <div
                  key={result.id}
                  className="group rounded-xl border-2 border-slate-100 bg-slate-50 p-4 transition-all hover:border-indigo-200 hover:bg-indigo-50 hover:shadow-md"
                >
                  <div className="mb-2 flex items-center justify-between">
                    <p className="font-bold text-slate-900">Тест #{result.test_id}</p>
                    <span
                      className={`rounded-full px-3 py-1 text-xs font-semibold ${
                        percentage >= 80
                          ? "bg-green-100 text-green-700"
                          : percentage >= 60
                            ? "bg-yellow-100 text-yellow-700"
                            : "bg-red-100 text-red-700"
                      }`}
                    >
                      {percentage}%
                    </span>
                  </div>
                  <div className="mb-2 flex items-center gap-2">
                    <span className="text-lg font-bold text-indigo-600">{result.score}</span>
                    <span className="text-slate-400">/</span>
                    <span className="text-slate-600">{result.total}</span>
                  </div>
                  <p className="text-xs text-slate-500">
                    {new Date(result.passed_at).toLocaleString("ru-RU")}
                  </p>
                </div>
              );
            })}
            {results.length === 0 && (
              <div className="rounded-xl border-2 border-dashed border-slate-200 bg-slate-50 p-8 text-center">
                <p className="text-slate-500">Нет попыток прохождения тестов</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Dashboard;


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
      <div className="rounded-2xl border border-slate-200 bg-white p-6 text-center">
        <p className="text-lg text-slate-700">Авторизуйтесь, чтобы видеть личный кабинет.</p>
        <Link to="/login" className="mt-4 inline-block rounded-xl bg-indigo-600 px-4 py-2 text-white">
          Перейти ко входу
        </Link>
      </div>
    );
  }

  return (
    <section className="grid gap-6 md:grid-cols-2">
      <ProgressSummary progress={progress} />
      <div className="rounded-xl border border-slate-200 bg-white p-5">
        <h3 className="text-lg font-semibold text-slate-900">История тестов</h3>
        <div className="mt-4 flex flex-col gap-3">
          {results.map((result) => (
            <div key={result.id} className="rounded-lg border border-slate-100 p-3 text-sm">
              <p className="font-semibold text-slate-800">Тест #{result.test_id}</p>
              <p className="text-slate-600">
                {result.score}/{result.total} • {new Date(result.passed_at).toLocaleString()}
              </p>
            </div>
          ))}
          {results.length === 0 && <p className="text-sm text-slate-500">Нет попыток</p>}
        </div>
      </div>
    </section>
  );
};

export default Dashboard;


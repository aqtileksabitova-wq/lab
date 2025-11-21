import type { Progress } from "../types";

const statusLabels: Record<Progress["status"], string> = {
  not_started: "Не начато",
  in_progress: "В процессе",
  completed: "Завершено",
};

const ProgressSummary = ({ progress }: { progress: Progress[] }) => {
  const completed = progress.filter((p) => p.status === "completed").length;
  const percent = progress.length ? Math.round((completed / progress.length) * 100) : 0;

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm text-slate-500">Прогресс</p>
          <p className="text-2xl font-semibold text-slate-900">{percent}%</p>
        </div>
        <div className="text-sm text-slate-500">
          {completed} из {progress.length} лекций
        </div>
      </div>
      <div className="mt-4 flex flex-col gap-2">
        {progress.map((item) => (
          <div key={item.lecture_id} className="flex items-center justify-between text-sm">
            <span>Лекция #{item.lecture_id}</span>
            <span className="font-medium text-slate-600">{statusLabels[item.status]}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProgressSummary;


import type { Progress } from "../types";

const statusLabels: Record<Progress["status"], string> = {
  not_started: "Не начато",
  in_progress: "В процессе",
  completed: "Завершено",
};

const ProgressSummary = ({ progress }: { progress: Progress[] }) => {
  const completed = progress.filter((p) => p.status === "completed").length;
  const inProgress = progress.filter((p) => p.status === "in_progress").length;
  const percent = progress.length ? Math.round((completed / progress.length) * 100) : 0;

  return (
    <div className="rounded-2xl border-2 border-slate-200 bg-white p-6 shadow-lg">
      <div className="mb-6 flex items-center gap-3">
        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-indigo-100 text-indigo-600">
          📊
        </div>
        <h3 className="text-xl font-bold text-slate-900">Прогресс обучения</h3>
      </div>
      <div className="mb-6">
        <div className="mb-2 flex items-center justify-between">
          <span className="text-sm font-semibold text-slate-600">Общий прогресс</span>
          <span className="text-2xl font-bold text-indigo-600">{percent}%</span>
        </div>
        <div className="h-4 overflow-hidden rounded-full bg-slate-200">
          <div
            className="h-full rounded-full bg-gradient-to-r from-indigo-500 to-purple-500 transition-all duration-500"
            style={{ width: `${percent}%` }}
          ></div>
        </div>
        <div className="mt-2 flex items-center gap-4 text-xs text-slate-500">
          <span>✓ Завершено: {completed}</span>
          <span>⏳ В процессе: {inProgress}</span>
          <span>○ Не начато: {progress.length - completed - inProgress}</span>
        </div>
      </div>
      <div className="space-y-2">
        <p className="text-sm font-semibold text-slate-700">Детали по лекциям:</p>
        <div className="max-h-64 space-y-2 overflow-y-auto">
          {progress.map((item) => {
            const statusColors = {
              completed: "bg-green-100 text-green-700 border-green-200",
              in_progress: "bg-yellow-100 text-yellow-700 border-yellow-200",
              not_started: "bg-slate-100 text-slate-600 border-slate-200",
            };
            return (
              <div
                key={item.lecture_id}
                className={`flex items-center justify-between rounded-lg border-2 p-3 text-sm transition-all ${statusColors[item.status]}`}
              >
                <span className="font-medium">Лекция #{item.lecture_id}</span>
                <span className="rounded-full px-2 py-1 text-xs font-semibold">
                  {statusLabels[item.status]}
                </span>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default ProgressSummary;


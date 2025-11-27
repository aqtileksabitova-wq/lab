import { Link } from "react-router-dom";
import type { Lecture } from "../types";

const LectureCard = ({ lecture }: { lecture: Lecture }) => (
  <Link
    to={`/lectures/${lecture.id}`}
    className="group flex flex-col gap-4 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all hover:scale-[1.02] hover:border-indigo-300 hover:shadow-xl"
  >
    <div className="flex items-start justify-between gap-4">
      <div className="flex-1">
        <div className="mb-2 inline-flex items-center gap-2 rounded-full bg-indigo-50 px-3 py-1">
          <span className="text-xs font-semibold text-indigo-600">Лекция #{lecture.id}</span>
        </div>
        <h3 className="text-xl font-bold text-slate-900 transition-colors group-hover:text-indigo-600">
          {lecture.title}
        </h3>
        <p className="mt-2 text-sm leading-relaxed text-slate-600">{lecture.short_description}</p>
      </div>
    </div>
    <div className="flex items-center text-sm font-semibold text-indigo-600 transition-all group-hover:translate-x-1">
      Перейти к лекции
      <span className="ml-2 transition-transform group-hover:translate-x-1">→</span>
    </div>
  </Link>
);

export default LectureCard;


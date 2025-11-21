import { Link } from "react-router-dom";
import type { Lecture } from "../types";

const LectureCard = ({ lecture }: { lecture: Lecture }) => (
  <div className="flex flex-col gap-3 rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
    <div>
      <h3 className="text-lg font-semibold text-slate-900">{lecture.title}</h3>
      <p className="text-sm text-slate-600">{lecture.short_description}</p>
    </div>
    <Link
      className="text-sm font-semibold text-indigo-600 hover:text-indigo-500"
      to={`/lectures/${lecture.id}`}
    >
      Перейти к лекции →
    </Link>
  </div>
);

export default LectureCard;


import type { Question } from "../types";

interface Props {
  question: Question;
  selected: number[];
  onSelect: (answerId: number) => void;
}

const TestQuestion = ({ question, selected, onSelect }: Props) => {
  const isMulti = question.question_type === "multi";
  return (
    <div className="group rounded-2xl border-2 border-slate-200 bg-white p-6 shadow-sm transition-all hover:border-indigo-300 hover:shadow-md">
      <div className="mb-4 flex items-start justify-between gap-4">
        <h4 className="text-lg font-bold leading-relaxed text-slate-900">{question.question_text}</h4>
        <span className="flex-shrink-0 rounded-full bg-indigo-100 px-3 py-1 text-xs font-semibold text-indigo-600">
          {isMulti ? "Множественный выбор" : "Один ответ"}
        </span>
      </div>
      <div className="space-y-3">
        {question.answers.map((answer) => {
          const isSelected = selected.includes(answer.id);
          return (
            <label
              key={answer.id}
              className={`group/answer flex cursor-pointer items-start gap-4 rounded-xl border-2 p-4 transition-all ${
                isSelected
                  ? "border-indigo-500 bg-indigo-50 shadow-md"
                  : "border-slate-200 bg-slate-50 hover:border-indigo-300 hover:bg-indigo-50/50"
              }`}
            >
              <input
                type={isMulti ? "checkbox" : "radio"}
                name={`question-${question.id}`}
                value={answer.id}
                checked={isSelected}
                onChange={() => onSelect(answer.id)}
                className="mt-1 h-5 w-5 cursor-pointer accent-indigo-600"
              />
              <span
                className={`flex-1 text-sm leading-relaxed ${
                  isSelected ? "font-semibold text-indigo-900" : "text-slate-700"
                }`}
              >
                {answer.answer_text}
              </span>
            </label>
          );
        })}
      </div>
      {question.explanation && (
        <div className="mt-4 rounded-lg border border-amber-200 bg-amber-50 p-3">
          <p className="text-xs font-medium text-amber-800">
            💡 <span className="font-semibold">Подсказка:</span> {question.explanation}
          </p>
        </div>
      )}
    </div>
  );
};

export default TestQuestion;


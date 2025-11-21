import type { Question } from "../types";

interface Props {
  question: Question;
  selected: number[];
  onSelect: (answerId: number) => void;
}

const TestQuestion = ({ question, selected, onSelect }: Props) => {
  const isMulti = question.question_type === "multi";
  return (
    <div className="rounded-lg border border-slate-200 bg-white p-4">
      <h4 className="font-semibold text-slate-900">{question.question_text}</h4>
      <div className="mt-3 flex flex-col gap-2">
        {question.answers.map((answer) => (
          <label
            key={answer.id}
            className="flex items-center gap-2 rounded-md border border-slate-200 p-2 hover:border-indigo-200"
          >
            <input
              type={isMulti ? "checkbox" : "radio"}
              name={`question-${question.id}`}
              value={answer.id}
              checked={selected.includes(answer.id)}
              onChange={() => onSelect(answer.id)}
            />
            <span className="text-sm text-slate-700">{answer.answer_text}</span>
          </label>
        ))}
      </div>
      {question.explanation && (
        <p className="mt-3 text-xs text-slate-500">Подсказка: {question.explanation}</p>
      )}
    </div>
  );
};

export default TestQuestion;


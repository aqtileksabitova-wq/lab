import { useState } from "react";
import { createLecture } from "../api/lectures";
import { createTest } from "../api/tests";
import useAuthStore from "../store/auth";

const AdminPanel = () => {
  const { user, token } = useAuthStore();
  const [lecturePayload, setLecturePayload] = useState({
    title: "",
    short_description: "",
    content: "",
  });
  const [testPayload, setTestPayload] = useState({
    lecture_id: 1,
    title: "",
    description: "",
    questionsJson: `[
  {
    "question_text": "Вопрос",
    "question_type": "single",
    "answers": [
      {"answer_text": "Ответ 1", "is_correct": true},
      {"answer_text": "Ответ 2", "is_correct": false}
    ]
  }
]`,
  });
  const [message, setMessage] = useState("");

  const handleLectureSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      await createLecture(lecturePayload);
      setMessage("Лекция создана");
    } catch (error) {
      setMessage("Ошибка при создании лекции");
      console.error(error);
    }
  };

  const handleTestSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const questions = JSON.parse(testPayload.questionsJson);
      await createTest({
        lecture_id: Number(testPayload.lecture_id),
        title: testPayload.title,
        description: testPayload.description,
        questions,
      });
      setMessage("Тест создан");
    } catch (error) {
      setMessage("Ошибка при создании теста (проверьте JSON)");
      console.error(error);
    }
  };

  if (!token) return <p>Авторизуйтесь, чтобы попасть в админку.</p>;
  if (!user) return <p>Загрузка профиля...</p>;
  if (user.role !== "admin") return <p>Доступ запрещён</p>;

  return (
    <section className="space-y-6">
      <h1 className="text-3xl font-bold text-slate-900">Админ-панель</h1>
      {message && <div className="rounded-lg border border-indigo-100 bg-indigo-50 p-3 text-indigo-700">{message}</div>}
      <div className="grid gap-6 md:grid-cols-2">
        <form onSubmit={handleLectureSubmit} className="space-y-4 rounded-2xl border border-slate-200 bg-white p-5">
          <h2 className="text-xl font-semibold text-slate-900">Новая лекция</h2>
          <input
            className="w-full rounded-lg border border-slate-200 p-2"
            placeholder="Заголовок"
            value={lecturePayload.title}
            onChange={(e) => setLecturePayload({ ...lecturePayload, title: e.target.value })}
            required
          />
          <input
            className="w-full rounded-lg border border-slate-200 p-2"
            placeholder="Краткое описание"
            value={lecturePayload.short_description}
            onChange={(e) => setLecturePayload({ ...lecturePayload, short_description: e.target.value })}
            required
          />
          <textarea
            className="h-40 w-full rounded-lg border border-slate-200 p-2"
            placeholder="Полный текст (Markdown)"
            value={lecturePayload.content}
            onChange={(e) => setLecturePayload({ ...lecturePayload, content: e.target.value })}
            required
          />
          <button className="rounded-lg bg-indigo-600 px-4 py-2 text-white">Сохранить лекцию</button>
        </form>

        <form onSubmit={handleTestSubmit} className="space-y-4 rounded-2xl border border-slate-200 bg-white p-5">
          <h2 className="text-xl font-semibold text-slate-900">Новый тест</h2>
          <input
            type="number"
            className="w-full rounded-lg border border-slate-200 p-2"
            placeholder="ID лекции"
            value={testPayload.lecture_id}
            onChange={(e) => setTestPayload({ ...testPayload, lecture_id: Number(e.target.value) })}
            required
          />
          <input
            className="w-full rounded-lg border border-slate-200 p-2"
            placeholder="Заголовок теста"
            value={testPayload.title}
            onChange={(e) => setTestPayload({ ...testPayload, title: e.target.value })}
            required
          />
          <input
            className="w-full rounded-lg border border-slate-200 p-2"
            placeholder="Описание"
            value={testPayload.description}
            onChange={(e) => setTestPayload({ ...testPayload, description: e.target.value })}
          />
          <textarea
            className="h-40 w-full rounded-lg border border-slate-200 p-2 font-mono text-xs"
            value={testPayload.questionsJson}
            onChange={(e) => setTestPayload({ ...testPayload, questionsJson: e.target.value })}
          />
          <button className="rounded-lg bg-indigo-600 px-4 py-2 text-white">Сохранить тест</button>
        </form>
      </div>
    </section>
  );
};

export default AdminPanel;


import { Link } from "react-router-dom";

const features = [
  "Интерактивные лекции по C++",
  "Тесты с автоматической проверкой",
  "Прогресс и история прохождений",
  "Админ-панель для управления контентом",
];

const Home = () => (
  <section className="space-y-10">
    <div className="rounded-3xl bg-gradient-to-r from-indigo-600 to-purple-600 p-10 text-white">
      <p className="text-sm uppercase tracking-wide text-indigo-100">cpp learn</p>
      <h1 className="mt-2 text-4xl font-bold">Учите C++ через лекции и тесты</h1>
      <p className="mt-4 text-lg text-indigo-100">
        Платформа объединяет теорию, практику и аналитику прогресса. Начните с базовых тем и доходите до уверенных
        решений.
      </p>
      <div className="mt-6 flex gap-4">
        <Link to="/lectures" className="rounded-full bg-white px-5 py-2 text-sm font-semibold text-indigo-600">
          Список лекций
        </Link>
        <Link to="/dashboard" className="rounded-full border border-white/30 px-5 py-2 text-sm font-semibold">
          Личный кабинет
        </Link>
      </div>
    </div>
    <div className="grid gap-4 md:grid-cols-2">
      {features.map((feature) => (
        <div key={feature} className="rounded-2xl border border-slate-200 bg-white p-6">
          <p className="text-base font-semibold text-slate-900">{feature}</p>
        </div>
      ))}
    </div>
  </section>
);

export default Home;


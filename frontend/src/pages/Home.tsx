import { Link } from "react-router-dom";

const features = [
  { text: "10 тематических лекций по C++", icon: "📚", color: "from-blue-500 to-cyan-500" },
  { text: "Тесты с автоматической проверкой", icon: "✅", color: "from-green-500 to-emerald-500" },
  { text: "Подборка видео с YouTube", icon: "🎥", color: "from-red-500 to-pink-500" },
  { text: "Онлайн-компилятор C++17/20", icon: "💻", color: "from-purple-500 to-indigo-500" },
  { text: "Прогресс и история прохождений", icon: "📊", color: "from-orange-500 to-amber-500" },
  { text: "Админ-панель для управления контентом", icon: "⚙️", color: "from-slate-500 to-gray-500" },
];

const Home = () => (
  <section className="space-y-12">
    <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-600 p-10 text-white shadow-2xl">
      <div className="relative z-10">
        <p className="text-sm uppercase tracking-wider text-indigo-100 opacity-90">cpp learn</p>
        <h1 className="mt-4 text-5xl font-bold leading-tight">Учите C++ через лекции и тесты</h1>
        <p className="mt-6 text-xl text-indigo-100 leading-relaxed">
          Платформа объединяет теорию, практику и аналитику прогресса. Начните с базовых тем и доходите до уверенных
          решений.
        </p>
        <div className="mt-8 flex flex-wrap gap-4">
          <Link
            to="/lectures"
            className="group rounded-full bg-white px-6 py-3 text-sm font-semibold text-indigo-600 shadow-lg transition-all hover:scale-105 hover:shadow-xl"
          >
            Список лекций →
          </Link>
          <Link
            to="/dashboard"
            className="rounded-full border-2 border-white/30 bg-white/10 px-6 py-3 text-sm font-semibold backdrop-blur-sm transition-all hover:bg-white/20 hover:border-white/50"
          >
            Личный кабинет
          </Link>
        </div>
      </div>
      <div className="absolute -right-20 -top-20 h-64 w-64 rounded-full bg-white/10 blur-3xl"></div>
      <div className="absolute -bottom-20 -left-20 h-64 w-64 rounded-full bg-white/10 blur-3xl"></div>
    </div>
    <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      {features.map((feature, index) => (
        <div
          key={feature.text}
          className="group relative overflow-hidden rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all hover:scale-[1.02] hover:shadow-xl"
        >
          <div className={`absolute inset-0 bg-gradient-to-br ${feature.color} opacity-0 transition-opacity group-hover:opacity-5`}></div>
          <div className="relative z-10 flex items-start gap-4">
            <div className="text-4xl">{feature.icon}</div>
            <p className="text-base font-semibold text-slate-900 leading-relaxed">{feature.text}</p>
          </div>
        </div>
      ))}
    </div>
  </section>
);

export default Home;


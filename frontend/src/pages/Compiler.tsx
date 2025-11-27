import axios from "axios";
import { useState } from "react";
import { runCompiler } from "../api/compiler";
import type { CompileResponse } from "../types";

const defaultSource = `#include <iostream>
#include <string>

int main() {
    // Входные данные можно задать прямо в коде
    int a = 10;
    int b = 20;
    
    std::cout << "Сумма " << a << " + " << b << " = " << (a + b) << std::endl;
    
    // Или использовать строки
    std::string name = "C++";
    std::cout << "Привет, " << name << "!" << std::endl;
    
    return 0;
}`;

const exampleWithInput = `#include <iostream>
#include <sstream>
#include <string>

int main() {
    // Пример: обработка входных данных из строки
    std::string input = "5 10 15 20";
    std::istringstream iss(input);
    
    int sum = 0;
    int num;
    while (iss >> num) {
        sum += num;
    }
    
    std::cout << "Сумма чисел: " << sum << std::endl;
    return 0;
}`;

const Compiler = () => {
  const [source, setSource] = useState(defaultSource);
  const [stdVersion, setStdVersion] = useState<"c++17" | "c++20">("c++20");
  const [result, setResult] = useState<CompileResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleRun = async () => {
    setError(null);
    setLoading(true);
    setResult(null);
    try {
      const response = await runCompiler({
        source,
        std: stdVersion,
      });
      setResult(response);
    } catch (err) {
      const message = axios.isAxiosError(err)
        ? (err.response?.data?.detail as string) ?? err.message
        : err instanceof Error
          ? err.message
          : "Не удалось выполнить компиляцию. Попробуйте ещё раз.";
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  // Определяем, есть ли ошибки компиляции или выполнения
  const hasCompileError = result && result.compile_stderr && result.compile_stderr.trim() !== "";
  const output = result
    ? hasCompileError
      ? result.compile_stderr
      : result.run_stdout || result.run_stderr || ""
    : "";

  return (
    <section className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-slate-900">Компилятор C++</h1>
          <p className="mt-1 text-sm text-slate-600">
            Онлайн-компилятор. Входные данные задавайте прямо в коде.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <select
            value={stdVersion}
            onChange={(event) => setStdVersion(event.target.value as "c++17" | "c++20")}
            className="rounded-lg border-2 border-slate-200 bg-white px-3 py-2 text-sm font-medium text-slate-800 focus:border-indigo-500 focus:outline-none"
          >
            <option value="c++20">C++20</option>
            <option value="c++17">C++17</option>
          </select>
          <button
            type="button"
            onClick={() => setSource(defaultSource)}
            className="rounded-lg border-2 border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50"
          >
            Пример 1
          </button>
          <button
            type="button"
            onClick={() => setSource(exampleWithInput)}
            className="rounded-lg border-2 border-slate-200 bg-white px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50"
          >
            Пример 2
          </button>
        </div>
      </div>

      <div className="grid gap-6 lg:grid-cols-2">
        {/* Левая колонка: Код */}
        <div className="space-y-4">
          <div className="rounded-lg border-2 border-slate-200 bg-white shadow-sm">
            <div className="flex items-center justify-between border-b border-slate-200 bg-slate-50 px-4 py-2">
              <span className="text-sm font-semibold text-slate-700">Код C++</span>
              <span className="text-xs text-slate-500">
                💡 Входные данные задавайте прямо в коде
              </span>
            </div>
            <textarea
              value={source}
              onChange={(event) => setSource(event.target.value)}
              rows={28}
              className="w-full resize-none border-0 bg-slate-900 px-4 py-3 font-mono text-sm text-slate-100 caret-indigo-400 focus:outline-none"
              placeholder="Введите код C++..."
            />
          </div>

          <button
            type="button"
            onClick={handleRun}
            disabled={loading}
            className="w-full rounded-lg bg-indigo-600 px-4 py-3 text-sm font-semibold text-white shadow-md transition-all hover:bg-indigo-700 disabled:opacity-50"
          >
            {loading ? (
              <span className="flex items-center justify-center gap-2">
                <span className="h-4 w-4 animate-spin rounded-full border-2 border-white border-t-transparent"></span>
                Выполнение...
              </span>
            ) : (
              "▶ Запустить"
            )}
          </button>
        </div>

        {/* Правая колонка: Вывод */}
        <div className="space-y-4">
          <div className="rounded-lg border-2 border-slate-200 bg-white shadow-sm">
            <div className="flex items-center justify-between border-b border-slate-200 bg-slate-50 px-4 py-2">
              <span className="text-sm font-semibold text-slate-700">Вывод</span>
              {result && (
                <span className="text-xs text-slate-500">
                  {result.exit_code === 0 ? (
                    <span className="text-green-600">✓ Успешно</span>
                  ) : hasCompileError ? (
                    <span className="text-red-600">✗ Ошибка компиляции</span>
                  ) : (
                    <span className="text-red-600">✗ Ошибка выполнения</span>
                  )}
                </span>
              )}
            </div>
            <div className="min-h-[500px] bg-slate-900 px-4 py-3">
              {loading ? (
                <div className="flex h-full items-center justify-center">
                  <div className="text-center">
                    <div className="mx-auto h-8 w-8 animate-spin rounded-full border-2 border-indigo-400 border-t-transparent"></div>
                    <p className="mt-2 text-sm text-slate-400">Выполнение...</p>
                  </div>
                </div>
              ) : error ? (
                <pre className="font-mono text-sm leading-relaxed text-red-400 whitespace-pre-wrap">
                  {error}
                </pre>
              ) : result ? (
                <pre className="font-mono text-sm leading-relaxed text-slate-100 whitespace-pre-wrap">
                  {output || (result.exit_code === 0 ? "Программа выполнена успешно" : "")}
                </pre>
              ) : (
                <div className="flex h-full items-center justify-center">
                  <p className="text-sm text-slate-500">
                    Вывод появится здесь после выполнения программы
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Compiler;



"""Static seed data for initial lectures and tests."""

from app.models.enums import QuestionType

LECTURES = [
    {
        "title": "Введение в C++",
        "short_description": "История языка, настройка окружения и первая программа.",
        "content": """
## История языка
C++ был создан Бьёрном Страуструпом как расширение C.

## Установка компилятора
- GCC (Linux/macOS/Windows с MinGW)
- MSVC (Visual Studio)

## Первая программа
```cpp
#include <iostream>
int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
```
## Структура программы
- Директивы `#include`
- Функция `main`
- Возврат `return`
""",
    },
    {
        "title": "Переменные и типы данных",
        "short_description": "Базовые типы и операции ввода/вывода.",
        "content": """
## Базовые типы
int, double, float, char, bool.

## Ввод и вывод
Используем `std::cin` и `std::cout`.

## Арифметические операции
Сложение, вычитание, умножение, деление, остаток.
""",
    },
    {
        "title": "Условия и циклы",
        "short_description": "if/else, switch и основные циклы.",
        "content": """
## if / else if / else
Позволяют выполнять ветвления.

## switch
Удобен для множества вариантов.

## Циклы
`for`, `while`, `do...while` для повторений.
""",
    },
]


TESTS = [
    {
        "lecture_index": 0,
        "title": "Тест: Введение в C++",
        "description": "Проверьте базовые знания о языке и компиляторах.",
        "questions": [
            {
                "question_text": "Кто является создателем языка C++?",
                "question_type": QuestionType.SINGLE,
                "explanation": "Бьёрн Страуструп создал C++ в Bell Labs.",
                "answers": [
                    {"answer_text": "Бьёрн Страуструп", "is_correct": True},
                    {"answer_text": "Деннис Ричи", "is_correct": False},
                    {"answer_text": "Гвидо ван Россум", "is_correct": False},
                ],
            },
            {
                "question_text": "Какой заголовок необходим для вывода в консоль?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "<cstdio>", "is_correct": False},
                    {"answer_text": "<iostream>", "is_correct": True},
                    {"answer_text": "<stdio.h>", "is_correct": False},
                ],
            },
            {
                "question_text": "Как называется основная точка входа программы?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "main", "is_correct": True},
                    {"answer_text": "start", "is_correct": False},
                    {"answer_text": "entry", "is_correct": False},
                ],
            },
            {
                "question_text": "Выберите корректные компиляторы C++.",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "GCC", "is_correct": True},
                    {"answer_text": "MSVC", "is_correct": True},
                    {"answer_text": "PyCompiler", "is_correct": False},
                ],
            },
            {
                "question_text": "Что делает оператор return 0 в main?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Возвращает управление ОС и сообщает об успешном завершении", "is_correct": True},
                    {"answer_text": "Завершает программу с ошибкой", "is_correct": False},
                    {"answer_text": "Перезапускает программу", "is_correct": False},
                ],
            },
            {
                "question_text": "Какая команда компилирует файл main.cpp с помощью g++?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "g++ main.cpp -o main", "is_correct": True},
                    {"answer_text": "python main.cpp", "is_correct": False},
                    {"answer_text": "node main.cpp", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие IDE подходят для разработки C++?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "CLion", "is_correct": True},
                    {"answer_text": "Visual Studio", "is_correct": True},
                    {"answer_text": "Photoshop", "is_correct": False},
                ],
            },
        ],
    },
    {
        "lecture_index": 1,
        "title": "Тест: Переменные и типы",
        "description": "Проверьте умение работать с типами данных.",
        "questions": [
            {
                "question_text": "Как объявить переменную типа int со значением 10?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "int value = 10;", "is_correct": True},
                    {"answer_text": "int value := 10;", "is_correct": False},
                    {"answer_text": "int value <- 10;", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие типы относятся к числовым с плавающей точкой?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "double", "is_correct": True},
                    {"answer_text": "float", "is_correct": True},
                    {"answer_text": "char", "is_correct": False},
                ],
            },
            {
                "question_text": "Как вывести значение переменной x на экран?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "std::cout << x;", "is_correct": True},
                    {"answer_text": "print(x);", "is_correct": False},
                    {"answer_text": "console.log(x);", "is_correct": False},
                ],
            },
            {
                "question_text": "Как считать значение из консоли в переменную a?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "std::cin >> a;", "is_correct": True},
                    {"answer_text": "input(a);", "is_correct": False},
                    {"answer_text": "scanf(a);", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие операции относятся к арифметическим?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "+", "is_correct": True},
                    {"answer_text": "-", "is_correct": True},
                    {"answer_text": "%", "is_correct": True},
                    {"answer_text": "&&", "is_correct": False},
                ],
            },
            {
                "question_text": "Каков размер типа bool в C++ (обычно)?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "1 байт", "is_correct": True},
                    {"answer_text": "4 байта", "is_correct": False},
                    {"answer_text": "8 байт", "is_correct": False},
                ],
            },
            {
                "question_text": "Что произойдёт при делении двух целых чисел?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Результат будет целым числом (отбрасывается дробная часть)", "is_correct": True},
                    {"answer_text": "Результат всегда double", "is_correct": False},
                    {"answer_text": "Произойдёт ошибка компиляции", "is_correct": False},
                ],
            },
        ],
    },
    {
        "lecture_index": 2,
        "title": "Тест: Условия и циклы",
        "description": "Проверьте контроль потока и циклы.",
        "questions": [
            {
                "question_text": "Как записать простое условие if?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "if (condition) { /* ... */ }", "is_correct": True},
                    {"answer_text": "if condition then", "is_correct": False},
                    {"answer_text": "if condition:", "is_correct": False},
                ],
            },
            {
                "question_text": "Когда использовать switch?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Когда нужно сравнить выражение со множеством констант", "is_correct": True},
                    {"answer_text": "Только для строк", "is_correct": False},
                    {"answer_text": "Чтобы заменить циклы", "is_correct": False},
                ],
            },
            {
                "question_text": "Выберите циклы, доступные в C++.",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "for", "is_correct": True},
                    {"answer_text": "while", "is_correct": True},
                    {"answer_text": "foreach", "is_correct": False},
                    {"answer_text": "do...while", "is_correct": True},
                ],
            },
            {
                "question_text": "Как остановить цикл досрочно?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "break;", "is_correct": True},
                    {"answer_text": "exit;", "is_correct": False},
                    {"answer_text": "stop;", "is_correct": False},
                ],
            },
            {
                "question_text": "Что делает оператор continue?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Переходит к следующей итерации цикла", "is_correct": True},
                    {"answer_text": "Полностью завершает цикл", "is_correct": False},
                    {"answer_text": "Завершает программу", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие части включает цикл for?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "Инициализация", "is_correct": True},
                    {"answer_text": "Проверка условия", "is_correct": True},
                    {"answer_text": "Изменение счётчика", "is_correct": True},
                    {"answer_text": "try/catch", "is_correct": False},
                ],
            },
            {
                "question_text": "Как выглядит цикл do...while?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "do { /* ... */ } while (condition);", "is_correct": True},
                    {"answer_text": "while { } do (condition);", "is_correct": False},
                    {"answer_text": "loop (condition) { }", "is_correct": False},
                ],
            },
        ],
    },
]


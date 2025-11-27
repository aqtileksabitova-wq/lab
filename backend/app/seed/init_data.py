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
- Clang/LLVM

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
        "short_description": "Базовые типы, ввод/вывод и преобразования.",
        "content": """
## Базовые типы
`int`, `double`, `float`, `char`, `bool`, `std::string`.

## Ввод и вывод
Используем `std::cin`, `std::cout`, манипуляторы форматирования.

## Арифметика и приведения типов
- Целочисленное и вещественное деление
- Неявные и явные преобразования (`static_cast`)
""",
    },
    {
        "title": "Условия и циклы",
        "short_description": "if/else, switch и основные циклы.",
        "content": """
## if / else if / else
Позволяют выполнять ветвления.

## switch
Удобен для множества вариантов (константные значения).

## Циклы
`for`, `while`, `do...while`, диапазонный `for` (C++11).
""",
    },
    {
        "title": "Функции и область видимости",
        "short_description": "Определение функций, параметры и возвращаемые значения.",
        "content": """
## Объявление и определение
```cpp
int sum(int a, int b);
int sum(int a, int b) { return a + b; }
```

## Передача аргументов
- По значению
- По ссылке (`int&`)
- По константной ссылке (`const std::string&`)

## Область видимости
Глобальная, локальная, статические переменные.
""",
    },
    {
        "title": "Массивы, строки и std::vector",
        "short_description": "Работа с непрерывными контейнерами и динамическими массивами.",
        "content": """
## Сырые массивы
```cpp
int arr[5] = {1,2,3,4,5};
```

## std::string
- Конкатенация
- Методы `size()`, `substr()`, `find()`

## std::vector
Динамический массив из `<vector>`, методы `push_back`, `emplace_back`, `at`.
""",
    },
    {
        "title": "Указатели и ссылки",
        "short_description": "Модель памяти, разыменование и владение ресурсами.",
        "content": """
## Указатели
`int* ptr = &value;` разыменование через `*ptr`.

## Ссылки
Безопасные псевдонимы переменных.

## RAII и умные указатели
- `std::unique_ptr`
- `std::shared_ptr`
""",
    },
    {
        "title": "Классы и объекты",
        "short_description": "Инкапсуляция, конструкторы и методы класса.",
        "content": """
## Определение класса
```cpp
class Vector2D {
public:
    Vector2D(double x, double y);
    double length() const;
private:
    double x_;
    double y_;
};
```

## Конструкторы и инициализация
Списки инициализации, конструкторы по умолчанию и копирования.

## Инкапсуляция
Модификаторы доступа, геттеры/сеттеры.
""",
    },
    {
        "title": "Наследование и полиморфизм",
        "short_description": "Базовые и производные классы, виртуальные методы.",
        "content": """
## Наследование
`class Dog : public Animal { ... };`

## Полиморфизм
Виртуальные функции, `override`, чисто виртуальные методы.

## Абстрактные классы и интерфейсы
Создание API без реализации.
""",
    },
    {
        "title": "Шаблоны и стандартная библиотека",
        "short_description": "Функции-шаблоны, классы-шаблоны и STL.",
        "content": """
## Шаблоны функций
```cpp
template <typename T>
T max_value(T a, T b) { return a > b ? a : b; }
```

## Контейнеры STL
`std::array`, `std::vector`, `std::map`, `std::unordered_map`.

## Алгоритмы
`std::sort`, `std::accumulate`, `std::for_each`.
""",
    },
    {
        "title": "Обработка ошибок и отладка",
        "short_description": "Исключения, static_assert и инструменты отладки.",
        "content": """
## Исключения
`try/catch`, собственные классы исключений.

## Диагностика
`assert`, `static_assert`, логирование.

## Отладка
GDB/LLDB, Visual Studio Debugger, Sanitizers.
""",
    },
]


TESTS = [
    {
        "lecture_title": "Введение в C++",
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
        "lecture_title": "Переменные и типы данных",
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
        "lecture_title": "Условия и циклы",
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
    {
        "lecture_title": "Функции и область видимости",
        "title": "Тест: Функции и область видимости",
        "description": "Проверьте понимание функций и областей видимости.",
        "questions": [
            {
                "question_text": "Как объявить функцию, которая принимает два int и возвращает int?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "int sum(int a, int b);", "is_correct": True},
                    {"answer_text": "function sum(a, b) return int;", "is_correct": False},
                    {"answer_text": "def sum(a: int, b: int) -> int;", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие способы передачи параметров существуют в C++?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "По значению", "is_correct": True},
                    {"answer_text": "По ссылке", "is_correct": True},
                    {"answer_text": "По указателю", "is_correct": True},
                    {"answer_text": "По имени", "is_correct": False},
                ],
            },
            {
                "question_text": "Что означает const перед параметром функции?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Параметр нельзя изменять внутри функции", "is_correct": True},
                    {"answer_text": "Параметр обязателен", "is_correct": False},
                    {"answer_text": "Параметр имеет постоянное значение", "is_correct": False},
                ],
            },
            {
                "question_text": "Как объявить функцию, которая не изменяет объект?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "void func() const;", "is_correct": True},
                    {"answer_text": "void const func();", "is_correct": False},
                    {"answer_text": "const void func();", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое область видимости?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Часть программы, где доступна переменная", "is_correct": True},
                    {"answer_text": "Размер переменной в памяти", "is_correct": False},
                    {"answer_text": "Тип переменной", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие области видимости существуют в C++?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "Глобальная", "is_correct": True},
                    {"answer_text": "Локальная", "is_correct": True},
                    {"answer_text": "Классовая", "is_correct": True},
                    {"answer_text": "Файловая", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое статическая переменная?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Переменная, которая сохраняет значение между вызовами функции", "is_correct": True},
                    {"answer_text": "Переменная, которая не может изменяться", "is_correct": False},
                    {"answer_text": "Переменная, которая существует только в одной функции", "is_correct": False},
                ],
            },
        ],
    },
    {
        "lecture_title": "Массивы, строки и std::vector",
        "title": "Тест: Массивы, строки и std::vector",
        "description": "Проверьте работу с контейнерами и строками.",
        "questions": [
            {
                "question_text": "Как объявить массив из 5 целых чисел?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "int arr[5];", "is_correct": True},
                    {"answer_text": "int[] arr = new int[5];", "is_correct": False},
                    {"answer_text": "arr = [0] * 5", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие методы есть у std::string?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "size()", "is_correct": True},
                    {"answer_text": "substr()", "is_correct": True},
                    {"answer_text": "find()", "is_correct": True},
                    {"answer_text": "append()", "is_correct": True},
                ],
            },
            {
                "question_text": "Как добавить элемент в конец std::vector?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "vec.push_back(value);", "is_correct": True},
                    {"answer_text": "vec.add(value);", "is_correct": False},
                    {"answer_text": "vec.append(value);", "is_correct": False},
                ],
            },
            {
                "question_text": "Как получить размер std::vector?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "vec.size()", "is_correct": True},
                    {"answer_text": "vec.length()", "is_correct": False},
                    {"answer_text": "vec.count()", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое std::vector?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Динамический массив из стандартной библиотеки", "is_correct": True},
                    {"answer_text": "Статический массив фиксированного размера", "is_correct": False},
                    {"answer_text": "Связанный список", "is_correct": False},
                ],
            },
            {
                "question_text": "Как объединить две строки в C++?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "str1 + str2", "is_correct": True},
                    {"answer_text": "str1.append(str2)", "is_correct": True},
                    {"answer_text": "str1.concat(str2)", "is_correct": False},
                ],
            },
            {
                "question_text": "Как безопасно получить элемент std::vector по индексу?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "vec.at(index)", "is_correct": True},
                    {"answer_text": "vec[index]", "is_correct": False},
                    {"answer_text": "vec.get(index)", "is_correct": False},
                ],
            },
        ],
    },
    {
        "lecture_title": "Указатели и ссылки",
        "title": "Тест: Указатели и ссылки",
        "description": "Проверьте понимание указателей и ссылок.",
        "questions": [
            {
                "question_text": "Как получить адрес переменной?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "&variable", "is_correct": True},
                    {"answer_text": "*variable", "is_correct": False},
                    {"answer_text": "$variable", "is_correct": False},
                ],
            },
            {
                "question_text": "Как разыменовать указатель?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "*ptr", "is_correct": True},
                    {"answer_text": "&ptr", "is_correct": False},
                    {"answer_text": "ptr.value", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое ссылка в C++?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Псевдоним переменной, который нельзя переназначить", "is_correct": True},
                    {"answer_text": "Указатель на переменную", "is_correct": False},
                    {"answer_text": "Копия переменной", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие умные указатели есть в C++?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "std::unique_ptr", "is_correct": True},
                    {"answer_text": "std::shared_ptr", "is_correct": True},
                    {"answer_text": "std::weak_ptr", "is_correct": True},
                    {"answer_text": "std::smart_ptr", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое RAII?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Идиома управления ресурсами через время жизни объекта", "is_correct": True},
                    {"answer_text": "Способ выделения памяти", "is_correct": False},
                    {"answer_text": "Тип указателя", "is_correct": False},
                ],
            },
            {
                "question_text": "Когда использовать std::unique_ptr?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Когда нужен единственный владелец ресурса", "is_correct": True},
                    {"answer_text": "Когда нужны несколько владельцев", "is_correct": False},
                    {"answer_text": "Когда нужен указатель на массив", "is_correct": False},
                ],
            },
            {
                "question_text": "Можно ли переназначить ссылку?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Нет, ссылка привязана к переменной при инициализации", "is_correct": True},
                    {"answer_text": "Да, можно изменить на другую переменную", "is_correct": False},
                    {"answer_text": "Только если она const", "is_correct": False},
                ],
            },
        ],
    },
    {
        "lecture_title": "Классы и объекты",
        "title": "Тест: Классы и объекты",
        "description": "Проверьте понимание ООП в C++.",
        "questions": [
            {
                "question_text": "Как объявить класс в C++?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "class MyClass { };", "is_correct": True},
                    {"answer_text": "class MyClass() { }", "is_correct": False},
                    {"answer_text": "def class MyClass:", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие модификаторы доступа есть в C++?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "public", "is_correct": True},
                    {"answer_text": "private", "is_correct": True},
                    {"answer_text": "protected", "is_correct": True},
                    {"answer_text": "internal", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое конструктор?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Специальная функция для инициализации объекта", "is_correct": True},
                    {"answer_text": "Функция для уничтожения объекта", "is_correct": False},
                    {"answer_text": "Обычная функция класса", "is_correct": False},
                ],
            },
            {
                "question_text": "Как объявить конструктор?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "ClassName();", "is_correct": True},
                    {"answer_text": "void ClassName();", "is_correct": False},
                    {"answer_text": "init ClassName();", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое деструктор?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Функция, вызываемая при уничтожении объекта", "is_correct": True},
                    {"answer_text": "Функция для создания объекта", "is_correct": False},
                    {"answer_text": "Функция для копирования объекта", "is_correct": False},
                ],
            },
            {
                "question_text": "Что означает const после метода класса?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Метод не изменяет состояние объекта", "is_correct": True},
                    {"answer_text": "Метод возвращает константу", "is_correct": False},
                    {"answer_text": "Метод нельзя вызывать", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое инкапсуляция?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Сокрытие деталей реализации и предоставление интерфейса", "is_correct": True},
                    {"answer_text": "Наследование свойств от другого класса", "is_correct": False},
                    {"answer_text": "Создание множества объектов одного класса", "is_correct": False},
                ],
            },
        ],
    },
    {
        "lecture_title": "Наследование и полиморфизм",
        "title": "Тест: Наследование и полиморфизм",
        "description": "Проверьте понимание наследования и полиморфизма.",
        "questions": [
            {
                "question_text": "Как объявить наследование в C++?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "class Derived : public Base { };", "is_correct": True},
                    {"answer_text": "class Derived extends Base { }", "is_correct": False},
                    {"answer_text": "class Derived(Base) { }", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие уровни наследования существуют в C++?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "public", "is_correct": True},
                    {"answer_text": "protected", "is_correct": True},
                    {"answer_text": "private", "is_correct": True},
                    {"answer_text": "internal", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое виртуальная функция?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Функция, которая может быть переопределена в производном классе", "is_correct": True},
                    {"answer_text": "Функция, которая не существует", "is_correct": False},
                    {"answer_text": "Функция, которая выполняется виртуально", "is_correct": False},
                ],
            },
            {
                "question_text": "Как объявить виртуальную функцию?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "virtual void func();", "is_correct": True},
                    {"answer_text": "void virtual func();", "is_correct": False},
                    {"answer_text": "void func() virtual;", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое чисто виртуальная функция?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Функция без реализации, делающая класс абстрактным", "is_correct": True},
                    {"answer_text": "Функция, которая ничего не делает", "is_correct": False},
                    {"answer_text": "Функция, которая всегда возвращает 0", "is_correct": False},
                ],
            },
            {
                "question_text": "Как объявить чисто виртуальную функцию?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "virtual void func() = 0;", "is_correct": True},
                    {"answer_text": "virtual void func() = null;", "is_correct": False},
                    {"answer_text": "virtual void func() pure;", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое полиморфизм?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Способность объектов разных типов обрабатываться через общий интерфейс", "is_correct": True},
                    {"answer_text": "Создание множества объектов", "is_correct": False},
                    {"answer_text": "Наследование от нескольких классов", "is_correct": False},
                ],
            },
        ],
    },
    {
        "lecture_title": "Шаблоны и стандартная библиотека",
        "title": "Тест: Шаблоны и STL",
        "description": "Проверьте знание шаблонов и стандартной библиотеки.",
        "questions": [
            {
                "question_text": "Как объявить шаблон функции?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "template <typename T> void func(T arg);", "is_correct": True},
                    {"answer_text": "template T void func(T arg);", "is_correct": False},
                    {"answer_text": "generic <T> void func(T arg);", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие контейнеры есть в STL?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "std::vector", "is_correct": True},
                    {"answer_text": "std::map", "is_correct": True},
                    {"answer_text": "std::unordered_map", "is_correct": True},
                    {"answer_text": "std::array", "is_correct": True},
                ],
            },
            {
                "question_text": "Как отсортировать std::vector?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "std::sort(vec.begin(), vec.end());", "is_correct": True},
                    {"answer_text": "vec.sort();", "is_correct": False},
                    {"answer_text": "sort(vec);", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое итератор?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Объект для доступа к элементам контейнера", "is_correct": True},
                    {"answer_text": "Тип контейнера", "is_correct": False},
                    {"answer_text": "Функция для поиска", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие алгоритмы есть в STL?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "std::sort", "is_correct": True},
                    {"answer_text": "std::find", "is_correct": True},
                    {"answer_text": "std::accumulate", "is_correct": True},
                    {"answer_text": "std::for_each", "is_correct": True},
                ],
            },
            {
                "question_text": "Как объявить шаблон класса?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "template <typename T> class MyClass { };", "is_correct": True},
                    {"answer_text": "class template MyClass<T> { }", "is_correct": False},
                    {"answer_text": "generic class MyClass<T> { }", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое std::map?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Ассоциативный контейнер, хранящий пары ключ-значение", "is_correct": True},
                    {"answer_text": "Динамический массив", "is_correct": False},
                    {"answer_text": "Очередь", "is_correct": False},
                ],
            },
        ],
    },
    {
        "lecture_title": "Обработка ошибок и отладка",
        "title": "Тест: Обработка ошибок и отладка",
        "description": "Проверьте знание обработки ошибок и отладки.",
        "questions": [
            {
                "question_text": "Как обработать исключение в C++?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "try { } catch (Exception& e) { }", "is_correct": True},
                    {"answer_text": "try { } except Exception:", "is_correct": False},
                    {"answer_text": "try { } finally { }", "is_correct": False},
                ],
            },
            {
                "question_text": "Как выбросить исключение?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "throw std::runtime_error(\"error\");", "is_correct": True},
                    {"answer_text": "raise RuntimeError(\"error\");", "is_correct": False},
                    {"answer_text": "throw new Exception(\"error\");", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие типы исключений есть в стандартной библиотеке?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "std::runtime_error", "is_correct": True},
                    {"answer_text": "std::logic_error", "is_correct": True},
                    {"answer_text": "std::invalid_argument", "is_correct": True},
                    {"answer_text": "std::file_error", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое assert?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Макрос для проверки условий во время выполнения", "is_correct": True},
                    {"answer_text": "Функция для вывода сообщений", "is_correct": False},
                    {"answer_text": "Тип исключения", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое static_assert?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Проверка условий во время компиляции", "is_correct": True},
                    {"answer_text": "Проверка условий во время выполнения", "is_correct": False},
                    {"answer_text": "Динамическая проверка", "is_correct": False},
                ],
            },
            {
                "question_text": "Какие инструменты отладки используются для C++?",
                "question_type": QuestionType.MULTI,
                "answers": [
                    {"answer_text": "GDB", "is_correct": True},
                    {"answer_text": "LLDB", "is_correct": True},
                    {"answer_text": "Visual Studio Debugger", "is_correct": True},
                    {"answer_text": "Python debugger", "is_correct": False},
                ],
            },
            {
                "question_text": "Что такое sanitizers?",
                "question_type": QuestionType.SINGLE,
                "answers": [
                    {"answer_text": "Инструменты для обнаружения ошибок памяти и undefined behavior", "is_correct": True},
                    {"answer_text": "Инструменты для очистки кода", "is_correct": False},
                    {"answer_text": "Типы исключений", "is_correct": False},
                ],
            },
        ],
    },
]

VIDEO_LECTURES = [
    {
        "title": "C++ Programming Course - freeCodeCamp",
        "short_description": "11-часовой интенсив по современному C++ от freeCodeCamp.",
        "youtube_id": "vLnPwxZdW4Y",
        "duration_minutes": 660,
        "channel": "freeCodeCamp.org",
    },
    {
        "title": "CppCon 2022: Kate Gregory — Embrace Modern C++",
        "short_description": "Доклад о практиках модернизации кода и идиомах C++20.",
        "youtube_id": "2ydhC0f2bGk",
        "duration_minutes": 65,
        "channel": "CppCon",
    },
    {
        "title": "Ranges in C++20 — Sy Brand",
        "short_description": "Практическое введение в `std::ranges` и новые алгоритмы.",
        "youtube_id": "2JDuwhVEzUI",
        "duration_minutes": 50,
        "channel": "ACCU Conference",
    },
    {
        "title": "Bjarne Stroustrup: The Essence of C++",
        "short_description": "Базовые принципы языка и эволюция C++ глазами автора.",
        "youtube_id": "86xWVb4XIyE",
        "duration_minutes": 75,
        "channel": "University of Texas",
    },
    {
        "title": "C++ STL Tutorial - Derek Banas",
        "short_description": "Подробный обзор стандартной библиотеки шаблонов C++.",
        "youtube_id": "Rub-JsjMhWY",
        "duration_minutes": 90,
        "channel": "Derek Banas",
    },
    {
        "title": "Modern C++ Features - Jason Turner",
        "short_description": "Обзор современных возможностей C++17 и C++20.",
        "youtube_id": "yG1OZ69H_-o",
        "duration_minutes": 60,
        "channel": "CppCon",
    },
    {
        "title": "C++ Smart Pointers Explained - The Cherno",
        "short_description": "Подробное объяснение умных указателей в современном C++.",
        "youtube_id": "U3XWwOm_E6Y",
        "duration_minutes": 25,
        "channel": "The Cherno",
    },
    {
        "title": "C++ Templates Tutorial - CodeBeauty",
        "short_description": "Практическое введение в шаблоны C++ для начинающих.",
        "youtube_id": "IzoFn3icosU",
        "duration_minutes": 45,
        "channel": "CodeBeauty",
    },
    {
        "title": "C++ Object Oriented Programming - Programming with Mosh",
        "short_description": "Основы объектно-ориентированного программирования в C++.",
        "youtube_id": "wN0x9eZLix4",
        "duration_minutes": 120,
        "channel": "Programming with Mosh",
    },
    {
        "title": "C++ Memory Management - Bo Qian",
        "short_description": "Управление памятью, указатели и умные указатели в C++.",
        "youtube_id": "3jZ9AwAaXEk",
        "duration_minutes": 55,
        "channel": "Bo Qian",
    },
    {
        "title": "C++ Exception Handling - The Cherno",
        "short_description": "Обработка исключений и лучшие практики в C++.",
        "youtube_id": "m9zawJC6q2E",
        "duration_minutes": 30,
        "channel": "The Cherno",
    },
    {
        "title": "C++ Lambda Expressions - CppNuts",
        "short_description": "Лямбда-выражения и функциональное программирование в C++.",
        "youtube_id": "mDBuIo4OXQk",
        "duration_minutes": 40,
        "channel": "CppNuts",
    },
]


import time

# Обычная функция для вычисления факториала
def factorial_iter(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Генератор для вычисления факториала
def factorial_gen(n):
    result = 1
    for i in range(2, n+1):
        result *= i
        yield result

# Рекурсивная функция для вычисления факториала
def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)

# Функция для замера времени работы другой функции
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

# Выбор числа для теста
n = 10

# Измерение времени работы обычной функции
fact_iter, time_iter = measure_time(factorial_iter, n)

# Измерение времени работы генератора (берем последний элемент последовательности)
start_time = time.time()
fact_gen = list(factorial_gen(n))[-1]  # Получаем последний факториал
time_gen = time.time() - start_time

# Измерение времени работы рекурсивной функции
fact_rec, time_rec = measure_time(factorial_rec, n)

# Результаты
print(f"Факториал через итерацию: {fact_iter}, время: {time_iter:.6f} сек")
print(f"Факториал через генератор: {fact_gen}, время: {time_gen:.6f} сек")
print(f"Факториал через рекурсию: {fact_rec}, время: {time_rec:.6f} сек")



# Декоратор

def typed(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Приводим аргументы к указанному типу
            new_args = [type(arg) for arg in args]
            return func(*new_args, **kwargs)
        return wrapper
    return decorator

# Функция сложения двух символов
@typed(type=str)
def add_two_symbols(a, b):
    return a + b

# Функция сложения трёх символов
@typed(type=int)
def add_three_symbols(a, b, c):
    return a + b + c

# Тестирование
print(add_two_symbols("3", 5))  # Ожидается: "35"
print(add_two_symbols(5, 5))    # Ожидается: "55"
print(add_two_symbols('a', 'b')) # Ожидается: "ab"

print(add_three_symbols(5, 6, 7))          # Ожидается: 18
print(add_three_symbols("3", 5, 0))        # Ожидается: 8
print(add_three_symbols(0.1, 0.2, 0.4))    # Ожидается: 0.700000000000000


# Лексикографическое возрастание 

# Шаги:
# Создадим словарь для названий чисел от 0 до 19.
# Получим список чисел, которые подаются на вход.
# Отсортируем эти числа в соответствии с их английскими названиями.
# Выведем отсортированные числа

# Словарь названий чисел
number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen'
}

# Входные данные: строка чисел, разделенных пробелами
input_data = input().split()

# Преобразуем строковые числа в целые
numbers = list(map(int, input_data))

# Сортируем числа по их названиям на английском
sorted_numbers = sorted(numbers, key=lambda x: number_names[x])

# Выводим результат
print(' '.join(map(str, sorted_numbers)))




# Калькулятор

def calculator():
    # Запрос у пользователя первого числа
    num1 = float(input("Введите первое число: "))

    # Запрос оператора
    operation = input("Выберите операцию (+, -, *, /): ")

    # Запрос у пользователя второго числа
    num2 = float(input("Введите второе число: "))

    # Выполнение операции
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Проверка деления на ноль
        if num2 != 0:
            result = num1 / num2
        else:
            return "Ошибка: Деление на ноль невозможно!"
    else:
        return "Ошибка: Неверная операция!"

    return f"Результат: {result}"

# Вызов калькулятора
print(calculator())

#Задание 1
from typing import Callable

def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел."""
    return a + b

def sub(a: float, b: float) -> float:
    """Возвращает разность двух чисел."""
    return a - b

def mult(a: float, b: float) -> float:
    """Возвращает произведение двух чисел."""
    return a * b

def div(a: float, b: float) -> float:
    """Возвращает частное двух чисел. Деление на ноль вызывает ошибку."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

def calculate(a: float, b: float, action: str) -> float:
    """
    Выполняет математическую операцию над двумя числами в зависимости от указанного действия.

    :param a: Первое число.
    :param b: Второе число.
    :param action: Символ математической операции ('+', '-', '*', '/').
    :return: Результат выполнения операции.
    :raises ValueError: Если указано неизвестное действие.
    """
    # Словарь для выбора функции в зависимости от действия
    actions: dict[str, Callable[[float, float], float]] = {
        '+': add,
        '-': sub,
        '*': mult,
        '/': div
    }

    # Проверка, есть ли указанное действие в словаре
    if action not in actions:
        raise ValueError(f"Неизвестное действие: {action}")

    # Выбор функции и выполнение операции
    func = actions[action]
    return func(a, b)

# Примеры вызова функции calculate

print(calculate(1, 5, action="+"))  # Выведет 6.0, так как 1 + 5 = 6
print(calculate(10, 2, action="-")) # Выведет 8.0, так как 10 - 2 = 8
print(calculate(4, 3, action="*"))  # Выведет 12.0, так как 4 * 3 = 12
print(calculate(8, 2, action="/"))  # Выведет 4.0, так как 8 / 2 = 4

# Попробуем деление на ноль
try:
    print(calculate(10, 0, action="/"))  # Выведет ошибку
except ValueError as e:
    print(e)  # Выведет "Деление на ноль невозможно."


#Усложнение
def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел."""
    return a + b

def sub(a: float, b: float) -> float:
    """Возвращает разность двух чисел."""
    return a - b

def mult(a: float, b: float) -> float:
    """Возвращает произведение двух чисел."""
    return a * b

def div(a: float, b: float) -> float:
    """Возвращает частное двух чисел. Деление на ноль вызывает ошибку."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

from typing import Callable, Dict

def calculate(a: float, b: float, action: str) -> float:
    """
    Выполняет математическую операцию над двумя числами в зависимости от действия.

    :param a: Первое число.
    :param b: Второе число.
    :param action: Символ действия ('+', '-', '*', '/').
    :return: Результат выполнения операции.
    :raises ValueError: Если действие не распознано.
    """
    # Определяем словарь с функциями
    operations: Dict[str, Callable[[float, float], float]] = {
        '+': add,
        '-': sub,
        '*': mult,
        '/': div
    }

    # Проверяем, есть ли действие в словаре
    if action not in operations:
        raise ValueError(f"Неизвестное действие: {action}")

    # Получаем функцию из словаря и выполняем её
    func = operations[action]
    return func(a, b)

print(calculate(5, 3, '+'))  # Выведет 8
print(calculate(10, 4, '-'))  # Выведет 6
print(calculate(6, 7, '*'))  # Выведет 42
print(calculate(20, 4, '/'))  # Выведет 5

try:
    print(calculate(10, 0, '/'))  # Выведет ошибку
except ValueError as e:
    print(e)  # Выведет "Деление на ноль невозможно."

#Задание 2
from typing import List, Optional, Union

def calculate_statistic(*args: float, stat: Optional[str] = None) -> Union[float, str]:
    """
    Вычисляет статистику по переданным числам.

    :param args: Произвольное количество чисел.
    :param stat: Строка, определяющая, какую статистику нужно вычислить ('avg', 'max', 'min', 'sum').
    :return: Среднее значение, максимальное значение, минимальное значение, сумма или сообщение об ошибке.
    :raises ValueError: Если список чисел пуст или неизвестный статистический параметр.
    """
    if not args:
        raise ValueError("Список чисел не может быть пустым.")

    # Функции для вычисления статистики
    stats = {
        'avg': lambda numbers: sum(numbers) / len(numbers),
        'max': lambda numbers: max(numbers),
        'min': lambda numbers: min(numbers),
        'sum': lambda numbers: sum(numbers)
    }

    # Проверяем, какой статистический параметр указан
    if stat is None or stat not in stats:
        raise ValueError(f"Неизвестный статистический параметр: {stat}")

    # Вычисляем статистику и возвращаем результат
    return stats[stat](args)

print(calculate_statistic(1, 2, 3, 4, 5, stat='avg'))  # Выведет 3.0
print(calculate_statistic(1, 2, 3, 4, 5, stat='max'))  # Выведет 5
print(calculate_statistic(1, 2, 3, 4, 5, stat='min'))  # Выведет 1
print(calculate_statistic(1, 2, 3, 4, 5, stat='sum'))  # Выведет 15

try:
    print(calculate_statistic(stat='avg'))  # Попробует вычислить среднее без чисел
except ValueError as e:
    print(e)  # Выведет "Список чисел не может быть пустым."

try:
    print(calculate_statistic(1, 2, 3, 4, 5, stat='unknown'))  # Попробует использовать неизвестный параметр
except ValueError as e:
    print(e)  # Выведет "Неизвестный статистический параметр: unknown"


#Работа с файлами. Задание 1
import random
import string
from datetime import datetime

def generate_random_string(length: int, probabilities: dict[int, float]) -> str:
    """
    Генерирует случайную строку с заданной длиной и добавляет к ней случайное число 
    из набора [200, 300, 400, 500] с заданными вероятностями.

    :param length: Длина случайной строки.
    :param probabilities: Словарь с вероятностями для чисел [200, 300, 400, 500].
    :return: Сгенерированная строка.
    """
    # Генерация случайной строки
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    
    # Выбор числа с учетом вероятностей
    numbers = [200, 300, 400, 500]
    weighted_numbers = [num for num in numbers for _ in range(int(probabilities[num] * 100))]
    chosen_number = random.choice(weighted_numbers)

    # Возвращаем строку с числом
    return f"{random_string}{chosen_number}"

def write_strings_to_file(filename: str, num_strings: int, string_length: int, probabilities: dict[int, float]) -> None:
    """
    Генерирует случайные строки и записывает их в файл.

    :param filename: Имя файла для записи.
    :param num_strings: Количество строк для генерации.
    :param string_length: Длина каждой случайной строки.
    :param probabilities: Словарь с вероятностями для чисел [200, 300, 400, 500].
    """
    with open(filename, 'w') as file:
        for _ in range(num_strings):
            # Генерация строки
            random_string = generate_random_string(string_length, probabilities)
            
            # Добавление текущей даты и времени
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            line = f"{timestamp} {random_string}\n"
            
            # Запись строки в файл
            file.write(line)

# Определяем вероятности
probabilities = {200: 0.3, 300: 0.2, 400: 0.25, 500: 0.25}

# Записываем строки в файл
write_strings_to_file('output.txt', num_strings=10, string_length=8, probabilities=probabilities)

#Задание 2
import os
import re
from typing import Dict

def write_lines_to_files(input_filename: str, output_filenames: Dict[int, str]) -> None:
    """
    Читает строки из входного файла и записывает их в отдельные файлы в зависимости от статуса в строке.

    :param input_filename: Имя входного файла для чтения.
    :param output_filenames: Словарь, где ключи - статусы, а значения - имена файлов для записи.
    """
    # Словарь для хранения файлов
    files = {status: open(filename, 'w') for status, filename in output_filenames.items()}

    try:
        # Чтение содержимого входного файла
        with open(input_filename, 'r') as infile:
            for line in infile:
                # Поиск статуса в конце строки
                match = re.search(r'(\d{3})$', line.strip())
                if match:
                    status = int(match.group(1))
                    if status in files:
                        # Запись строки в соответствующий файл
                        files[status].write(line)
    finally:
        # Закрытие всех файлов
        for file in files.values():
            file.close()

# Имя входного файла
input_filename = 'output.txt'

# Словарь с именами выходных файлов для каждого статуса
output_filenames = {
    200: 'status_200.txt',
    300: 'status_300.txt',
    400: 'status_400.txt',
    500: 'status_500.txt'
}

# Выполняем разбиение строк по файлам
write_lines_to_files(input_filename, output_filenames)

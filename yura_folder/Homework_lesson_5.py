# Задание 1 

# def add(number1, number2):
#     return number1 + number2

# def sub(number1, number2):
#     return number1 - number2

# def mult(number1, number2):
#     return number1 * number2

# def div(number1, number2):
#     if number2 != 0:
#         return number1 / number2
#     else:
#         return "Ошибка: деление на ноль!"

# def calculate(a, b, action):
#     operations = {
#         '+': add,
#         '-': sub,
#         '*': mult,
#         '/': div
#     }

#     if action in operations:
#         return operations[action](a, b)
#     else:
#         return "Ошибка: "
    
# result = calculate(20, 34, action="+")
# print(result)



# Задание 2

# def calculate_stat(*args, **kwargs):
#     if len(args) ==0:
#         return "Error"

#     operations = {
#         "avg": lambda numbers: sum(numbers) / len(numbers),  # Среднее
#         "sum": lambda numbers: sum(numbers),                # Сумма
#         "max": lambda numbers: max(numbers),                # Макс
#         "min": lambda numbers: min(numbers),                # Мин
#         "count": lambda numbers: len(numbers),              # Количество
#     }
#     stat = kwargs.get("stat", "avg")

#     if stat in operations:
#         return operations[stat](args)  # Вызываем нужную функцию для вычисления статистики
#     else:
#         return f"Error: '{stat}'"

# result1 = calculate_stat(1, 2, 3, 4, 5, 6, 7, stat="avg")  # Ожидается 4
# result2 = calculate_stat(1, 2, 3, 4, 5, 6, 7, stat="sum")  # Ожидается 28
# result3 = calculate_stat(1, 2, 3, 4, 5, 6, 7, stat="max")  # Ожидается 7
# result4 = calculate_stat(1, 2, 3, 4, 5, 6, 7, stat="min")  # Ожидается 1

# print(result1) 
# print(result2)  
# print(result3)  
# print(result4)

# Задание 3

import random
import string
from datetime import datetime

def generate_random_string(length=10):
    letters = string.ascii_letters                                            # Использование заглавных и строчных
    return ''.join(random.choice(letters) for i in range(length))

def append_random_number():
    numbers = [200, 300, 400, 500]
    probabilities = [0.1, 0.2, 0.3, 0.4]                      # Вероятности для каждого числа
    return random.choices(numbers, probabilities)[0]          # Возврат числа с учетом вероятности

def write_to_file(filename, num_lines):
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            random_string = generate_random_string()          # Генерация случайной строки

            number = append_random_number()                   # Добавляем случайное число с заданной вероятностью

            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')   # Получаем текущее время

            line = f"{current_time} {random_string} {number}\n"     # Формируем строку с датой, строкой и числом

            f.write(line)                  # Записываем строку в файл done

            print(f"Строка добавлена в файл и на экран: {line.strip()}")


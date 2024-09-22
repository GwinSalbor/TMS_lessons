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

# Генерация случайной строки и выбор случайного числа с вероятностями
def generate_line():
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))  # Генерация строки
    number = random.choices([200, 300, 400, 500], [0.1, 0.2, 0.3, 0.4])[0]           # Выбор числа с вероятностями
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')                      # Текущее время
    return f"{current_time} {random_string} {number}"                                # Финальная строка

# Запись строк в файл
def write_to_file(filename, num_lines):
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            line = generate_line()         # Генерируем строку
            f.write(line + '\n')           # Записываем в файл
            print(f"Строка: {line}")       # Выводим на экран

# Пример использования
write_to_file('random_strings.txt', 10)


### ФУНКЦИИ И АРГУМЕНТЫ
### Задание 1

### Вариант 1

# first_num = float(input("Введите первое значение: "))
# second_num = float(input("Введите второе значение: "))
# action = input("Какое действие провести +, -, *, / ?: ")


# def calculate(first_num: float, second_num: float, action) -> float:
#     """
#     Args:
#         first_num (float): Первое значение вводимое с клавиатуры
#         second_num (float): Второе значение вводимое с клавиатуры
#         action (any): Математическое действие, которое требуется произвести с введенными значениями (+, -, *, /)

#     Returns:
#         result (float): Возвращает итоговое значение после проводимого математического действия
#     """
#     def add(first_num: float, second_num: float) -> float:
#         """Возвращает сумму двух чисел"""
#         return first_num + second_num
    
#     def sub(first_num: float, second_num: float) -> float:
#         """Возвращает разность двух чисел"""
#         return first_num - second_num
    
#     def mult(first_num: float, second_num: float) -> float:
#         """Возвращает произведение двух чисел"""
#         return first_num * second_num
    
#     def div(first_num: float, second_num: float) -> float:
#         """Возвращает частное двух чисел"""
#         if second_num == 0:
#             return "На нуль делить нельзя!"
#         return first_num / second_num
    

#     ###Вариант выполнения задания через цикл
#     if action == "+":
#         return add(first_num, second_num)
#     elif action == "-":
#         return sub(first_num, second_num)
#     elif action == "*":
#         return mult(first_num, second_num)
#     elif action == "/":
#         return div(first_num, second_num)
#     else:
#         return "Неверная операция"
    
# result = calculate(first_num, second_num, action)
# print(f"Результат: {result}")

### Вариант 2

# def calculate() -> float:
#     """
#     Args:
#         first_num (float): Первое значение вводимое с клавиатуры
#         second_num (float): Второе значение вводимое с клавиатуры
#         action (any): Математическое действие, которое требуется произвести с введенными значениями (+, -, *, /)

#     Returns:
#         result (float): Возвращает итоговое значение после проводимого математического действия
#     """
#     def add(first_num: float, second_num: float) -> float:
#         """Возвращает сумму двух чисел"""
#         return first_num + second_num
    
#     def sub(first_num: float, second_num: float) -> float:
#         """Возвращает разность двух чисел"""
#         return first_num - second_num
    
#     def mult(first_num: float, second_num: float) -> float:
#         """Возвращает произведение двух чисел"""
#         return first_num * second_num
    
#     def div(first_num: float, second_num: float) -> float:
#         """Возвращает частное двух чисел"""
#         if second_num == 0:
#             return "На нуль делить нельзя!"
#         return first_num / second_num

#     first_num = float(input("Введите первое значение: "))
#     second_num = float(input("Введите второе значение: "))
#     action = input("Какое действие провести +, -, *, / ?: ")

#     ###Вариант исполнения с использованием словаря

#     actions= {'+': add, '-': sub, '*': mult, '/': div}

#     if action in actions:
#         result = actions[action](first_num, second_num)
#         print(f"Результат: {result}")
#     else:
#         print("Ошибка: недопустимая операция")
        
# calculate()

##Задание 2

# def calculate_statistic(*args: float, **kwargs) -> float:
#     """Вычисляет статистику по переданным числам.
#     Parameters:
#          args (float): Произвольное количество чисел
#     Returns:
#          result: Возвращает общую сумму, среднее, максимальное, минимальное значение и общее количество после проводимого математического действия
#      """
    
#     # Функции для вычисления статистики
#     stat = kwargs.get('stat')
#     avg = sum(args) / len(args)
#     total_sum = sum(args)
#     maximum = max(args)
#     minimum = min(args)
#     count = len(args)

#     #Возврат результата
#     if stat == 'avg':
#         return f"Average: {avg}"
#     elif stat == 'sum':
#         return f"Sum: {total_sum}"
#     elif stat == 'max':
#         return f"Max: {maximum}"
#     elif stat == 'min':
#         return f"Min: {minimum}"
#     elif stat == 'count':
#         return f"Count: {count}"


# print(calculate_statistic(1, 2, 3, 4, 6, 8, 9, 5, 6, 7, stat="avg"))
# print(calculate_statistic(1, 2, 3, 4, 5, 6, 7, stat="sum"))
# print(calculate_statistic(1, 2, 3, 4, 5, 6, 7, stat="max"))
# print(calculate_statistic(1, 2, 3, 4, 5, 6, 7, stat="min"))
# print(calculate_statistic(1, 2, 3, 4, 5, 6, 7, stat="count"))

### РАБОТА С ФАЙЛАМИ

### Задание 1

import random
import string
from datetime import datetime

# Функция для генерации случайной строки
def gen_rand_str(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Функция для добавления числа с определенной вероятностью
def probability(probabilities):
    numbers = [200, 300, 400, 500]
    return random.choices(numbers, weights=probabilities, k=1)
# Функция для записи строк в файл
def write(filename, num_lines, probabilities):
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            # Генерация случайной строки
            random_string = gen_rand_str()
            
            # Добавление числа в конец строки с заданной вероятностью
            random_number = probability(probabilities)
            
            # Добавление текущей даты и времени в начало строки
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Формирование итоговой строки
            final_string = f"{current_time} {random_string} {random_number}"
            
            # Запись строки в файл
            file.write(final_string + '\n')

# Задаем вероятности для чисел 200, 300, 400, 500
probabilities = [0.1, 0.2, 0.3, 0.4]  # 10% для 200, 20% для 300, 30% для 400, 40% для 500
write('output.txt', 25, probabilities)

# ###Задание 2

def split_file_by_status(input_filename):
    # Открываем исходный файл для чтения
    with open(input_filename, 'r') as infile:
        # Открываем четыре файла для записи строк со статусами
        with open('status_200.txt', 'w') as file_200, \
             open('status_300.txt', 'w') as file_300, \
             open('status_400.txt', 'w') as file_400, \
             open('status_500.txt', 'w') as file_500:

            # Проходим по каждой строке в исходном файле
            for line in infile:
                # # Убираем лишние пробелы и перевод строки
                # line = line.strip()

                # Разбиваем строку по пробелам, чтобы извлечь статус (последний элемент)
                parts = line.split()

                # Получаем статус, который находится в конце строки
                status = parts[-1]

                # В зависимости от статуса записываем строку в соответствующий файл
                if status == '[200]':
                    file_200.write(line + '\n')
                elif status == '[300]':
                    file_300.write(line + '\n')
                elif status == '[400]':
                    file_400.write(line + '\n')
                elif status == '[500]':
                    file_500.write(line + '\n')
                else:
                    print(f"Неизвестный статус: {status}")
split_file_by_status('output.txt')
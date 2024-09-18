import string
import random
# 1.	Напишите функции add, sub, mult, div для функции calculate,
# Add, sub, mult, div функции должны выполнять математические операции сложения, вычитания, умножения и деления
# функция calculate должна внутри себя вызывать эти функции в зависимотси от переданных параметров
# Пример вызова:
# calculate(1,5, action=”+”) - вызовет внутри функции calculate функцию add и посчитает сумму

# def add (number1:int, number2:int) -> int:
#     """Возвращает сумму двух чисел."""
#     return number1 + number2

# def sub (number1:int, number2:int) -> int:
#     """Возвращает расзность двух чисел."""
#     return number1 + number2

# def mult (number1:int, number2:int) -> int:
#     """Возвращает произведение двух чисел."""
#     return number1 * number2

# def div (number1:int, number2:int) -> int:
#     """Возвращает результат от деления двух чисел."""
#     if number2 == 0:
#         return "Ошибка! На ноль делить нельзя"
#     return number1 / number2

# def calculate (number1:int, number2:int, action:str) -> int:
#     """
#     Функция для выполнения математической операции в зависимости от переданного действия.
    
#     :param a: Первое число.
#     :param b: Второе число.
#     :param action: Строка, определяющая действие ('+', '-', '*', '/').
#     :return: Результат выполнения операции или сообщение об ошибке.
#     """
#     if action == "+":
#         return add(number1, number2)

#     elif action == "-":
#         return sub(number1, number2)

#     elif action == "*":
#         return mult(number1, number2)

#     elif action == "/":
#         return div(number1, number2)

#     else:
#         return "Пока не умею"


# print(calculate(2, 0, "/"))

# 2.	Напишите функцию calculate_statistic, которая принимает на вход список чисел и возвращает среднее значение, 
# максимальное значение, минимальное значение сумму 
# и тд (можете что-то придумать сами не обязательно но будет полезно).



def calculate_statistic(*args:int, **kwargs:dict) -> float:
    """
    Функция для вычисления статистических показателей на основе переданных чисел.
    
    :param args: Произвольное количество чисел.
    :param kwargs: Именованные параметры для выбора статистического показателя.
    :return: Запрашиваемый статистический показатель или сообщение об ошибке.
    """
    value = kwargs.get("value", None)

    if not args:
        return "Ошибка: числа не переданы!"
    
    elif value== "sum":
        return sum(args)
    
    elif value == "avg":
        return sum(args) / len(args)
    
    elif value == "max":
        return max(args)
    
    elif value == "min":
        return min(args)
       
    else:
        return "Непонятно, что хотите"



# Примеры вызова функции
print(calculate_statistic(5, 5, 6, 7, 8, 9, 10, value="avg"))  
print(calculate_statistic(5, 5, 6, 7, 8, 9, 10, value="sum"))  
print(calculate_statistic(5, 5, 6, 7, 8, 9, 10, value="max"))  
print(calculate_statistic(5, 5, 6, 7, 8, 9, 10, value="min"))  
print(calculate_statistic(5, 5, 6, 7, 8, 9, 10, value="unknown"))
print(calculate_statistic(value="sum"))

# Работа с файлами

# 1.	Создайте функцию которая будет генерировать случайные строки с помощью функции рандом random.choice() - и модуля string который я описал в подсказках 
# создайте функцию которая будет записывать строки в файл
# в цикле for сгенерируйте несколько строк и запишите их в файл, в случайном порядке добавляйте к строке в конце числа 200, 300, 400, 500

def generate_random_string(length=10):
    """Генерирует случайную строку заданной длины."""
    letters = string.ascii_letters  # Буквы (как строчные, так и заглавные)
    return ''.join(random.choice(letters) for i in range(length))

def write_strings_to_file(num_strings=5):
    """Записывает случайные строки в файл."""
    numbers = [200, 300, 400, 500]
    with open('lev_folder/test.txt', 'w+') as file:
        for _ in range(num_strings):
            random_string = generate_random_string()
            random_number = random.choice(numbers)  # Выбираем случайное число
            file.write(f"{random_string}{random_number}\n")  # Записываем строку в файл


write_strings_to_file()

# 2.	Создайте программу, которая читает содержимое текстового файла который вы сгенерировали в задании выше 
# и разбивает его на несколько файлов для статусов 200, 300, 400, 500 - соответственно, 
# в зависимости от того какой статус находится в конце строки.

def split_file_by_status(input_filename='lev_folder/test.txt'):
    """Читает файл и разбивает его на несколько файлов по статусам."""
    status_files = {
        200: open('lev_folder/status_200.txt', 'w'),
        300: open('lev_folder/status_300.txt', 'w'),
        400: open('lev_folder/status_400.txt', 'w'),
        500: open('lev_folder/status_500.txt', 'w')
    }

    try:
        with open(input_filename, 'r') as file:
            for line in file:
                # Извлекаем статус из конца строки
                status = line.strip()[-3:]  # Предполагаем, что статус всегда в конце строки
                if status.isdigit() and int(status) in status_files:
                    status_files[int(status)].write(line)  # Записываем строку в соответствующий файл
    except FileNotFoundError:
        print(f"Файл {input_filename} не найден.")
    finally:
        # Закрываем все открытые файлы
        for file in status_files.values():
            file.close()


split_file_by_status()
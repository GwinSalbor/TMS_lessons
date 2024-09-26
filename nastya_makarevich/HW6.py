# # #Задание_1
# # """
# # Напишите функции add, sub, mult, div для функции calculate,
# # Add, sub, mult, div функции должны выполнять математические операции сложения, вычитания, умножения и деления
# # функция calculate должна внутри себя вызывать эти функции в зависимотси от переданных параметров
# # Пример вызова:
# # calculate(1,5, action=”+”) - вызовет внутри функции calculate функцию add и посчитает сумму.
# # """
# # def add(x, y):
# #     return x + y
# # def sub(x, y):
# #     return x - y
# # def mult(x, y):
# #     return x * y
# # def div(x, y):
# #     return x / y if y != 0 else "Error!"
# #
# #
# # def calculate():
# #     x = int(input('Введите значение х: '))
# #     y = int(input('Введите значение y: '))
# #     action = input('Выберите действие +, -, *, /: ')
# #
# #     if action == '+':
# #         return add(x, y)
# #     elif action == '-':
# #         return sub(x, y)
# #     elif action == '*':
# #         return mult(x, y)
# #     elif action == '/':
# #         return div(x, y)
# #     else:
# #         return 'Error!'
# #
# # print(calculate())
# #
# #вариант 2
# # def calculate(a, b):
# #     add = a + b
# #     sub = a - b
# #     mult = a * b
# #     div = a / b
# #     return add, sub, mult, div
# # num1 , num2 = int(input('Введите значение a: ')), int(input('Введите значение b: '))
# # add, sub, mult, div = calculate(num1, num2)
# # print(
# #     f'Сложение: {add}\n'
# #     f'Вычитание: {sub}\n'
# #     f'Умножение: {mult}\n'
# #     f'Деление: {div:.2f}\n'
# # )
#
# #Задание_2
# """
# Напишите функцию calculate_statistic, которая принимает на вход список чисел и возвращает среднее значение,
# максимальное значение, минимальное значение сумму и тд
# (можете что-то придумать сами не обязательно но будет полезно).
# Реализуйте обработку произвольного числа аргументов с помощью *args
# и поддержите именованные параметры с помощью **kwargs, чтобы можно было задавать настройки поиска значения.
# Пример вызова:
# calculate_statistic(1,2,3,4,5,6,7, stat=”avg”) - вернет среднее значение введенных чисел и это 4
# calculate_statistic(1,2,3,4,5,6,7, stat=”sum”) - вернет сумму 28
# """
# # def calculate_statistic(*args, **kwargs):
# #     statistic = kwargs.get('statistic')
# #
# #     if statistic == 'sum':
# #         return sum(args)
# #     elif statistic == 'avg':
# #         return sum(args) / len(args)
# #     elif statistic == 'min':
# #         return min(args)
# #     elif statistic == 'max':
# #         return max(args)
# #
# #
# # print(calculate_statistic(1, 2, 3, 4, 5, 6, 7, statistic='sum'))
# # print(calculate_statistic(1, 2, 3, 4, 5, 6, 7, statistic='avg'))
# # print(calculate_statistic(1, 2, 3, 4, 5, 6, 7, statistic='min'))
# # print(calculate_statistic(1, 2, 3, 4, 5, 6, 7, statistic='max'))
#
# #Работа с файлами
# #Задание 1
# """
# Создайте функцию которая будет генерировать случайные строки с помощью функции рандом random.choice()
# - и модуля string который я описал в подсказках
# создайте функцию которая будет записывать строки в файл
# в цикле for сгенерируйте несколько строк и запишите их в файл,
# в случайном порядке добавляйте к строке в конце числа 200, 300, 400, 500
#
# """
# import random
# import string
# from datetime import datetime
#
# def gen_rand_str(length=10):
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for i in range(length))
# def probability(probabilities):
#     numbers = [200, 300, 400, 500]
#     return random.choices(numbers, weights=probabilities, k=1)
# def write(filename, num_lines, probabilities):
#     with open(filename, 'w') as file:
#         for _ in range(num_lines):
#             random_string = gen_rand_str()
#             random_number = probability(probabilities)
#             current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             final_string = f"{current_time} {random_string} {random_number}"
#             file.write(final_string + '\n')
#
# probabilities = [0.1, 0.2, 0.3, 0.4]  # 10% для 200, 20% для 300, 30% для 400, 40% для 500
# write('output.txt', 25, probabilities)
#
# #Задание_2
# """
# Создайте программу, которая читает содержимое текстового файла который вы сгенерировали
# в задании выше и разбивает его на несколько файлов для статусов 200, 300, 400, 500
# - соответственно, в зависимости от того какой статус находится в конце строки.
# """
#
# def file_new(input_filename):
#
#     with open(input_filename, 'r') as infile:
#
#         with open('status_200.txt', 'w') as file_200, \
#              open('status_300.txt', 'w') as file_300, \
#              open('status_400.txt', 'w') as file_400, \
#              open('status_500.txt', 'w') as file_500: \
#
#             for line in infile:
#                 parts = line.split()
#                 status = parts[-1]
#                 if status == '[200]':
#                     file_200.write(line + '\n')
#                 elif status == '[300]':
#                     file_300.write(line + '\n')
#                 elif status == '[400]':
#                     file_400.write(line + '\n')
#                 elif status == '[500]':
#                     file_500.write(line + '\n')
#                 else:
#                     print(f"Неизвестный статус: {status}")
# # file_new('output.txt')
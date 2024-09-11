"""
Создайте функцию которая будет генерировать случайные строки с помощью функции рандом random.choice()
- и модуля string который я описал в подсказках
создайте функцию которая будет записывать строки в файл
в цикле for сгенерируйте несколько строк и запишите их в файл,
в случайном порядке добавляйте к строке в конце числа 200, 300, 400, 500
Усложнение:
1) сделайте так, чтобы можно было задавать вероятности с которыми в конце строки будет значение  200, 300, 400, 500
2) добавьте в начало каждой строки дату и время используя модуль datetime с прошлого урока

"""

import random
import string
import datetime


def add_string():
    return ''.join(random.choice(string.ascii_letters) for s in range(20))


def writing(data):
    with open('test.txt', 'a') as f:
        f.write(data + '\n')


def add_number():
    numbers = [200, 300, 400, 500]
    return str(random.choices(numbers, weights=[10, 11, 2, 5])[0])


for _ in range(10):
    new_string = add_string()
    new_number = add_number()

    time_stamp = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')

    final_string = f"You have added your text on {time_stamp} {new_string} {new_number}"
    writing(final_string)


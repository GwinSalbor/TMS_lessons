"""
Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
Напишите программу, которая будет выводить уникальное число.
"""

numbers = [1, 5, 2, 9, 2, 9, 1,]


def func(numbers):
    for number in numbers:
        count = 0
        for i in numbers:
            if number == i:
                count += 1
        if count == 1:
            return number


update = func(numbers)
print(update)

"""
Напишите генератор, который принимает список
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
и возвращает новый список только с положительными числами.
"""

my_list = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


def positive_nums():
    for number in my_list:
        if number > 0:
            yield number


new_list = list(positive_nums())
print(new_list)





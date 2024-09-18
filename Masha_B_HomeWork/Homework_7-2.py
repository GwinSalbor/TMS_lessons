"""
Создать lambda функцию, которая принимает на вход список имен
и выводит их в формате "Hello, {name}" в другой список
"""

new_list = ['Masha', 'Tony', 'Jessica', 'Harry', 'Hermione']
my_func = list(map(lambda name: 'Hello, ' + name, new_list))
print(my_func)
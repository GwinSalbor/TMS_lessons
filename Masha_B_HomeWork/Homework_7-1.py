"""
Создать lambda функцию, которая принимает на вход имя и выводит его в формате "Hello, {name}"
"""

first_func = lambda name: 'Hello, {name}'.format(name=name)
print(first_func('Masha'))

"""
or
"""

second_func = lambda name: f'Hello, {name}'
print(second_func('Tony'))
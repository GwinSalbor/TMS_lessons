"""
Напишите функции add, sub, mult, div для функции calculate,
Add, sub, mult, div функции должны выполнять математические операции сложения, вычитания, умножения и деления
функция calculate должна внутри себя вызывать эти функции в зависимотси от переданных параметров
Пример вызова:
calculate(1,5, action=”+”) - вызовет внутри функции calculate функцию add и посчитает сумму
    Усложнение: Реализуйте выбор action с помощью словаря вы можете использовать в словаре как ключ строку 
    с символом математического действия, а в значение положить функцию
"""


def add(values: int) -> int:

    """
    Вычисляет и возвращает сумму принимаемых на вход int чисел
    """

    values_of_add = 0

    for i in values:
        values_of_add += i

    return values_of_add


def sub(values: int) -> int:

    """
    Вычисляет и возвращает разность принимаемых на вход int чисел
    """

    values_of_sub = values[0] * 2

    for i in values:
        values_of_sub -= i
        
    return values_of_sub


def mult(values: int) -> int:

    """
    Вычисляет и возвращает произведение принимаемых на вход int чисел
    """

    values_of_mult = 1

    for i in values:
        values_of_mult *= i

    return values_of_mult


def div(values: int) -> float:

    """
    Вычисляет и возвращает частное принимаемых на вход int чисел
    """

    values_of_div = values[0] ** 2

    for i in values:
        if i != 0:
            values_of_div /= i
        else:
            return 'в значениях есть 0, деление невозможно'
        
    return values_of_div


def calculate(*args: int, **kwargs: dict):

    """
    Принимает на вход int числа и dict словарь, состоящий из {действие : "математический знак вычисления"}.
    Возвращает результат функций add, sub, mult, div
    """

    values_of_choise = kwargs.get(''.join(list(kwargs.keys())))

    match values_of_choise:
        case "+":
            return add(args)
        case "-":
            return sub(args)
        case "*":
            return mult(args)
        case "/":
            return div(args)
        

print(calculate(1,3,5,7,9,11,13,15,0,19,21, action="/"))
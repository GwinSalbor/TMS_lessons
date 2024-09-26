"""
Напишите функции add, sub, mult, div для функции calculate,
Add, sub, mult, div функции должны выполнять математические операции сложения, вычитания, умножения и деления
функция calculate должна внутри себя вызывать эти функции в зависимотси от переданных параметров
Пример вызова:
calculate(1,5, action=”+”) - вызовет внутри функции calculate функцию add и посчитает сумму.
"""


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2 if num2 != 0 else "Division by zero is IMPOSSIBLE!"


def calculate():
    num1 = int(input('Enter a number: '))
    action = input('Enter action +, -, *, /: ')
    num2 = int(input('Enter a number: '))

    if action == '+':
        return add(num1, num2)
    elif action == '-':
        return sub(num1, num2)
    elif action == '*':
        return mult(num1, num2)
    elif action == '/':
        return div(num1, num2)
    else:
        return "Error!"


print(calculate())




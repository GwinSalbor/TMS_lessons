     #Функции и аргументы
# # Задание 1.1
# def add(Var_1, Var_2):
#     return Var_1 + Var_2
# def sub(Var_1, Var_2):
#     return Var_1 - Var_2
# def mult(Var_1, Var_2):
#     return Var_1 * Var_2
# def div(Var_1, Var_2):
#     return Var_1 / Var_2 \
#         if Var_2 != 0 \
#         else "Деление на 0 невозможно!"
# def calculate():
#     Var_1 = int(input('Введите значение: '))
#     Var_2 = int(input('Введите значение: '))
#     action = input('Выбор функции +, -, *, /: ')
#     if action == '+':
#         return add(Var_1, Var_2)
#     elif action == '-':
#         return sub(Var_1, Var_2)
#     elif action == '*':
#         return mult(Var_1, Var_2)
#     elif action == '/':
#         return div(Var_1, Var_2)
#     else:
#         return "Ошибка!"
# print(calculate())

# Задание 1.2

def calculate_statistics(*args, **kwargs):
    stat = kwargs.get('stat')

    if stat == 'sum':
        return sum(args)
    elif stat == 'avg':
        return sum(args) // len(args)
    elif stat == 'max':
        return max(args)
    elif stat == 'min':
        return min(args)
    else:
        return 'Доступные функции sum, avg, max, min'

print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='sum'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='avg'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='max'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='min'))

#Работа с файлами
#1.1


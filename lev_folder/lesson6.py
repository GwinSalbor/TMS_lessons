# def funct(first_arg,second_arg,third_arg, first_position_arg=123):
#     print(first_arg)
#     print(second_arg)
#     print(third_arg)
#     print(first_position_arg)
#     # print(args)
#     # print(kwargs)

# funct(second_arg=1,first_arg=2,third_arg =3, first_position_arg=5)

# def func1(a,b,c=123):
#     print(a,b,c)

# func1(1,2)

# def func_with_not_defined_amount_of_args(*args, **kwargs):
#     print(type(args))
#     print(type(kwargs))

# func_with_not_defined_amount_of_args(1,2,3,"random_string", hello="hello", random_value = 1)


# def calculate_total_sum_of_ints(*args, **kwargs):
#     result = 0
#     for i in args:
#         result += i
#     print(result)
# calculate_total_sum_of_ints(1,2,3, hello=1231245123123)



# def func(a, b):
#     print(a,b)

# func(1,2)

# Global example ________________________________________________________________________

# x = 10  # глобальная переменная

# def change_global():
#     a = 123
#     global x  # указываем, что хотим изменить глобальную переменную x
#     x = 20  # изменяем глобальную переменную
#     print("hello")

# change_global()
# print(x)

# # Local example ________________________________________________________________________
# a = 123
# def list(any_value):
#     print(any_value)

# list("aasdasd")
# print(x)

# Nonlobal example ________________________________________________________________________
# global_var = 1
# x = 5
# def outer_function():
#     # non_local_val = 5  # переменная в области видимости внешней функции
    
#     def inner_function():
#         # local_var = 10
#         # print(global_var) # ???
#         # print(non_local_val) # ???
#         print(local_var) # ???
#         # nonlocal x  # указываем, что хотим изменить переменную 'x' из внешней функции
#         # x = 10  # изменяем переменную 'x' во внешней функции
#         # print(x)
    
#     inner_function()
#     # print(x)  # Вывод: 10

# outer_function()


# Annotations example ________________________________________________________________________
# functions 
# def hello1(name: str) -> str:
#     """
#     name: str указывает, что параметр name должен быть строкой.
#     -> str указывает, что функция возвращает строку
#     """
#     return "Hello, " + name


# ## variables
# age: int = 25
# height: float = 1.88
# name: str = "Alice"
# list_val: list = []


# from typing import List, Dict, Set, Optional, Any

# names: List[Any] = ["Alice", "Bob", "Charlie"]
# ages: Dict[str, int] = {"Alice": 25, "Bob": 30}
# ids: Set[int] = {100000001, 100000002, 100000003}

# # comprehensions example ________________________________________________________________________
# # list comprehensions
# squares = [x**2 for x in range(10)]
# print(squares) 

# evens = [x if x % 2 == 0 else 10 for x in range(10)]
# asdqwe = []
# for x in range(10):
#     if x % 2 == 0:
#         asdqwe.append(x)
#     else:
#         asdqwe.append(10)
# print(asdqwe)


# print(evens)

# evens = [x for x in range(10) if x % 2 == 0]
# asdqwe = []
# for x in range(10):
#     if x % 2 == 0:
#         asdqwe.append(x)
# print(asdqwe)


# combinations = [(x, y) for x in range(1, 4) for y in range(4, 7)]
# print(combinations)
# combinations1 = []
# for x in range(1, 4):
#     for y in range(4, 7):
#         combinations1.append((x, y))
# print(combinations1)

# words = ["apple", "banana", "cherry"]
# first_letters = [word[0:3] for word in words]
# print(first_letters)

# set_gen = {x**2 for x in range(10)}
# print(set_gen)
# print(type(set_gen))
# dict_gen = {x: x**2 for x in range(10)}
# print(dict_gen)
# print(type(dict_gen))
# gen_expression = (x**2 for x in range(10))
# print(list(gen_expression))
# print(next(gen_expression))
# print(next(gen_expression))
# print(type(gen_expression))

# files example ________________________________________________________________________


# file = open('yaroslav/example.txt', 'r')

# for line in file:
#     print(line, end="")
# file.close()


# with open('/Users/yaroslav/Documents/pythonProject/TMS_lessons/yaroslav/example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('yaroslav/example.txt', 'w') as file:
#     file.write("AKSDJKLADSJKLJADS")

# with open('yaroslav/example1.txt', 'a') as file:
#     file.write("ASLKFJASKLD:JASLKDJ\n")

# with open('yaroslav/example1.txt', 'w+') as file:
#     for i in range(10000):
#         if i % 10 == 0:
#             file.write("\n")
#             file.write(f"|  {i} : {i**2}  |")
#         else:
#             file.write(f"|  {i} : {i**2}  |")

file = open('yaroslav/example.txt', 'r')

text = file.read()

file.close()

list_of_names = [
    "Dzina", "Masha", "Nastya", "Anton", "Anna",
    "Andrey", "Arina", "Elena", "Roman","Gleb",
    "Lev", "Nikolay", "Polina", "Yrua", "Anton"
]
print(text)
with open('yaroslav/invite.txt', 'a+') as file:
    for asd in list_of_names:
        invite_text = text.format(qwesad = asd)
        print(invite_text)
        file.write(invite_text + "\n")
    
    file.write("end of file" + "\n")
    file.seek(0)
    print(file.read())

print(file.read())



# s = "hello i invite you {name}, {sur}".format(name = "asd", sur = "jadklsfkldf")
# print(s)
# with open('example.txt', 'a+') as file:
#     file.write("Adding more content.\n")
#     file.seek(0)
#     print(file.read())


# with open('yaroslav/example.txt', 'r') as file:
#     print(file.readline())
#     print(file.readline())
#     file.seek(0)
#     print(file.read())\



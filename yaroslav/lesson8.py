

import time
def decorator(fun): # 1 в функцию можно передавать другую функцию, 2 функция может возвращать другую функцию
    def inner(*args, **kwargs): # *args, **kwargs 
        begining = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"execution time: {end-begining}")
        return result
    return inner

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
@decorator
def run_recursion():
    print(factorial(100))
@decorator
def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
@decorator
def fact_gen(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    yield res


print(fact(100))
run_recursion()

# def fun(s):
#     if len(s) > 10:
#         return s
#     else:
#         s += "a"
#         return fun(s)

# print(fun(""))




# # def outer_function(x):
# #     v = 12
# #     def inner_function(y):
# #         return x + y + v  # x запомнено из outer_function
# #     return inner_function

# # # Создаем замыкание
# # closure = outer_function(10)

# # # Вызываем внутреннюю функцию, которая "помнит" значение x = 10
# # print(closure(5))  # Выведет 15


# # oil_call = 10
# # def ingrediens(ing1, ing2, ing3, ing5):
# #     ing3 *= oil_call # переменная соханена в памяти для функии cook, сохраненные переменные (ing1, ing2, ing3)
# #     ing4 = 123 # переменная ing4 удалена после завершнеие функции ingrediens() как и ing5
# #     def cook(dish):
# #         ing6 = 12
# #         nonlocal ing2
# #         ret_s = f"{dish} callories = {ing1+ing2 +ing3}"
# #         ing2 = 54
# #         return ret_s
# #     return cook

# # # ing1, ing2, ing3, ing5 локальные для функции ingrediens
# # # ing1, ing2, ing3, ing5
# # soup = ingrediens(3, 6, 4, 5345)

# # print(soup("gaspacho"))
# # print(soup("borsh"))


# # def ingrediens():
# #     ing1 = 3
# #     def cook(dish):
# #         ing2 = 12
# #         nonlocal ing1
# #         ret_s = f"{dish} callories = {ing1+ing2}"
# #         ing1 += 10 # closure и увеличится после каждого выплднения cook (она не будет удалена, 
# #         # так как не принадлежит к локальной области видимости функции cook)
# #         ing2 += 1000 # локальная и увеличится но забудется после выполнения функции cook
# #         return ret_s
# #     return cook
# # # print(ingrediens()("a"))

# # soup = ingrediens()

# # print(soup("gaspacho"))
# # print(soup("borsh"))
# # print(soup("borsh1"))
# # print(soup("borsh2"))


# # def decorator_function(wrapped_func):
# #     def wrapper():
# #         print('Входим в функцию-обёртку')
# #         print('Оборачиваемая функция: ', wrapped_func)
# #         print('Выполняем обернутую функцию...')
# #         wrapped_func()
# #         print('Выходим из обёртки')
# #     return wrapper


# # @decorator_function
# # def Func_To_WraP(arg1, arg2):
# #     print("HELLO")

# # Func_To_WraP()


# import time
# def decorator(fun): # 1 в функцию можно передавать другую функцию, 2 функция может возвращать другую функцию
#     def inner(*args, **kwargs): # *args, **kwargs 
#         begining = time.time()
#         result = fun(*args, **kwargs)
#         end = time.time()
#         print(f"execution time: {end-begining}")
#         return result
#     return inner


# @decorator
# def fun(n):
#     time.sleep(n)


# fun(1)
# fun(4)

# print(a)
# print(decorator(fun1)(4,2))
# # @decorator
# # def fun2(zxc, cvb):
# #     print("fun2")
# #     return zxc/cvb
# # @decorator
# # def fun3(dfg, ert):
# #     print("fun3")
# #     return dfg/ert

# # print(fun1(4,2))
# # print(fun2(4,0))
# # print(fun3(4,0))


# def count(iters): # передача параметров для декоратора
#     def decorator(func): # передача декорируемой функции
#         def wrapper(*args, **kwargs): # передача аргументов функции
#             for i in iters:
#                 res = func(i) 
#                 if res == 0:
#                     print("no work")
#                 elif res == 1:
#                     print("less work")
#                 elif res == 2:
#                     print("work")
#         return wrapper
#     return decorator

# @count([-1, 10, 15, 20, 59, 100])
# @decorator
# def func(age):
#     if age < 12:
#         print("you soooo young")
#         return 0
#     elif age > 12 and age < 18:
#         print("you can work no more than 4h")
#         return 1
#     elif age >18 and age< 60:
#         print("lets work")
#         return 2
#     else:
#         print("rest and peace")
#         return 0


# def func1():
#     count()
#     any_dec()


# func()


# from functools import wraps

# def fake(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         pass
#     return inner

# @fake
# def power(a:int,b:int):
#     """
#     Hello i multiply a to b
#     """
#     print(a*b)

# def fake1(func):
#     def inner(*args, **kwargs):
#         pass
#     return inner
# @fake1
# def power1(a:int,b:int):
#     """
#     Hello i multiply a to b
#     """
#     print(a*b)


# print("Name", power.__name__)
# print("Annotations", power.__annotations__)
# print("Documentation", power.__doc__)

# print("Name", power1.__name__)
# print("Annotations", power1.__annotations__)
# print("Documentation", power1.__doc__)
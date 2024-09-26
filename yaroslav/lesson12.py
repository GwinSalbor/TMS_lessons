# l1 = [1,2,3]
# # s1 = {1,2,3}
# # d1 = {1:1, 2:2}

# # l1.append(4)
# # s1.add(3)
# # d1.update({3:3})

# print("for")
# for i in range(4):
#     print(i)

# # a = True
# print("while")
# # number = 1
# # import time
# i = 0
# while i < 4:
#     print(i)
#     i += 1
    

# def dec(fun):
#     def inner(*args, **kwargs):
#         return fun(*args, **kwargs)
#     return inner




# class Open_file:

#     def __enter__():
#         f = open("example.txt", "rwx")

#     def __exit__():
#         f.close()


# with open("example.txt", "rwx") as f:
#     f.read()

# from functools import reduce
# product = reduce((lambda x, y: x + y), [1, 2, 3, 4])
# print(product)
# # Output: 24
# b = 1



# def multiply(num1): # внешняя функция
#     var = 10 # не запомним это значение
#     def inner(num2): # замыкание
#         return num1 * num2
# #     return inner

# # print(multiply(4))
# # # <function multiply.<locals>.inner at 0x100418550>
# # print(multiply(4)(5)) # 20

# # func = multiply(4)
# # print(func(6))




# def gen(val):
#     for i in range(val):
#         yield i

# a = [0,1,2,3,4]
# print(a[0])
# print("start iter")
# for i in a:
#     print(i)
# b = gen(5)
# print(next(b))
# print(next(b))
# print("start gen")
# for i in b:
#     print(i)


# try:
#     f = open("asd")
# except ZeroDivisionError as e:
#     print(e)
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# class Hero: # Объявление класса
#     def __init__(self, name): # Oбъявление метода конструктора
#         self.name = name 

#     @staticmethod
#     def print_name(asd):
#         print("I am", asd)

# a = Hero("name")
# a.print_name("asd")

# def fun1():
#     a = 1

#     print("fun old_val")
#     print(a)
#     def f2():
#         nonlocal a
#         a = 2
#         print("f2")
#         print(a)
    
#     f2()
#     print("fun")
#     print(a)
# fun1()
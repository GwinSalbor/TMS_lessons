# def fun(any_func):
#     print(any_func("hello"))

# def inner(input_str):
#     return input_str+ " " + "world"

# # fun(inner)

# a = fun
# a(inner)

# print(list(map(lambda x: x+1+2+3, [1,2,3,4,5])))

# l1 = [1,2,]
# print(type(l1))
# lis = iter(l1)
# print(type(lis))
# print(next(lis))
# print(next(lis))
# print(next(lis))
# print("__________")
# gen = map(lambda x: x, [1,2])
# for i in gen:
#     print(i)

# def ret(asd: int) -> int:
#     if isinstance(asd, int):
#         raise TypeError("AAAAAAAA!!!")
#     return 5
# print(ret())
# # simple_list = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
# from typing import List
# def gen() -> Generator[int]:
#     if True:
#         for i in range(10):
#             yield i
#     else:
#         print("end")

# runner = gen()
# print(runner)
# print(type(runner))
# print(next(runner))

# def create_generator():
#     mylist = range(3)
#     for i in mylist:
#         yield i * i

# mygenerator = create_generator()
# for i in mygenerator:
#     print(i)
# print(next(mygenerator))
# print(next(mygenerator))
# print(next(mygenerator))
# print(next(mygenerator))


# for ind in ["a", "b", "c"]:
#     print(ind)

# for ind, value in enumerate(["a", "b", "c"]):
#     print(ind, value)


# for i in range(start=0, stop=10, step=2):
#     print(i)

# def gen_for_seq(seq: list):
#     count = 0
#     for i in seq:
#         count +=1 
#         yield count, i

# gen1 = gen_for_seq(["a", "b", "c"])
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

# def gen_with_logic(fuc, iterations):
#     for i in range(iterations):
#         yield fuc(i)

# gen2 = gen_with_logic(lambda x: x**2, 10)
# for i in gen2:
#     print(i)


# gen = (i/100 for i in range(100))

# print(type(gen), gen)

# print(next(gen))
# print(next(gen))

# def gen_for_seq(seq: list):
#     for i in seq:
#         yield i

# gen1 = gen_for_seq([1,2,3,4,5])
# print(list(gen1))

# def func(x):
#     return x
# lambda x: x

# def func():
#     for i in range(10):
#         yield i
# (i for i in range(10))

# gen = {(i/100 for i in range(10))}
# print(gen)


# try:
#     print(3/3)
#     print(3/2)
#     # raise Exception("I have error in my code")
#     # raise TypeError("Error")
#     print(3/1)
#     # print(3/0)
# except ZeroDivisionError as e:  
#     print("Деление на 0")
#     print(e)
# except TypeError as e:
#     print("type error")
#     print(e)
# except Exception as e:
#     print("any error")
#     print(e)
# finally:
#     print("all ok")

# try:
#     logic
# except Exception_Type:
#     exception_logic
# finally:
#     end of logic

# text = "hello how are you?"
# def encode(text, step):
#     """
#     1) пройтись по каждой букве текста
#     2) узнать позицию функцией ord()
#     3) добавить шаг к позиции буквы
#     3.1) конец алфавита
#     3.2) спец-символы
#     4) получить букву по позиции chr()
#     5) собрать и вернуть текст
#     """
#     return encoded_text

"abc!!".isalpha()
"bcd!!"
# encode("asd", 3)

a = 9
c = 5
if a >=10:
    c = 100
else: 
    c = 200
print(c)
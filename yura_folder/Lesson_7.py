# def fun(any_func):
#     print(inner("hello"))

# def inner(input_str):
#     return input_str+ " " + "world"

# fun(inner)


# оиличие return от yield
# def ret():
#     for i in range(5):
#         return i 
# print(ret())
# print(ret())
# print(ret())
# print(ret())

# def gen():
#     for i in range(5):
#         yield i
# runner = gen()
# print(next(runner))
# print(next(runner))
# print(next(runner))
# print(next(runner))


# def ret():
#     for i in range(3):
#         return i 
# print(ret())





# def create_generator():
#     mylist = range(3)
#     for i in mylist:
#         yield i * i

# mygenerator = create_generator()
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
#     for ii in seq:
#         count +=1
#         yield count, i 

# gen1 = gen_for_seq(["a", "b", "c"])
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))

# gen2 = gen_with_logic(lambda x: x**2, 10)
# for i in gen2:
#     print(i)


# gen = (i/100 for i in range(100))
# print(type(gen), gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))


# try:
#     print(3/3)
#     print(3/2)
#     print(3/1)
#     print(3/0)
# except ZeroDivisionError as e: 
#     print("Деление на 0")
#     print(e)
# except Exception as e:
#     print(e)

# print("asdasdasd")



def caesar_decoder(text, shift):
    decoded_text = ""
    
    for char in text:
        # Если символ - буква
        if char.isalpha():
            # Определяем сдвиг в зависимости от регистра (A-Z или a-z)
            offset = ord('A') if char.isupper() else ord('a')
            # Сдвигаем букву на нужное количество позиций
            decoded_char = chr((ord(char) - offset - shift) % 26 + offset)
            decoded_text += decoded_char
        else:
            # Если это не буква, просто добавляем символ
            decoded_text += char

    return decoded_text
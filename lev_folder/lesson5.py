import random
import datetime


# def new_func(name):
#     prefix = "hello, "
#     end = ", how you doing?"
#     return prefix + name + end

# prefix = "hello, "
# end = ", how you doing?"
# print(prefix + "yaroslav" + end)

# prefix = "hello, "
# end = ", how you doing?"
# print(prefix + "Anna" + end)

# ans_for_yar = new_func("yaroslav")
# ans_for_ann = new_func("Anna")
# print(ans_for_yar)
# print(new_func("Anna"))

# def add(x, y):
#     temp_val = x * 3
#     return temp_val + y

# print(add("hello ", "world"))
# print(add(1, 3))

def mul_3(x):
    return x * 3

# def del_6(x):
#     return x /6

# def gen(x):
#     x = mul_3(x)
#     x = del_6(x)
#     return x

# print(gen(12))
    

# def print_dict():
#     lst_str = ['один', 'два', 'три', 'четыре']
#     lst_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#     lst_names = ["one", "two"]
#     zipped = list(zip(lst_num, lst_str, lst_names))
#     print(zipped)

# print_dict()

# def cm_to_meter(val: int) -> float:
#     """
#     This function convert centimeters to meters!
#     """
#     return val / 100

# print(cm_to_meter(15))

# list_1 = [1,2,3]


list_of_names = [
    "Dzina", "Masha", "Nastya", "Anton", "Anna",
    "Andrey", "Arina", "Elena", "Roman","Gleb",
    "Lev", "Nikolay", "Polina", "Yrua", "Anton"
]
# def asdqwesad(val):
#     return len(val)

# print(map(asdqwesad, list_of_names))
# map_val = map(asdqwesad, list_of_names)

# print(map_val)


# def mul_2_and_to_string(val):
#     """discription """
#     return str(val*2)
# # ans_list = list(map(fun, list_of_names))
# # print(ans_list[0])
# # print(ans_list[1])

# print(dict([(1,2,)]))



# print(random.choice(list_of_names))

# error_data = random.randint(1, 18)

# correct_data = random.randint(19, 60)

# import datetime
# import random
# error_data = random.randint(1, 28)
# date = datetime.datetime(2023, 2, error_data)
# print(date)

from datetime import datetime

date_str = "23-11-12 10:56:34"
birthday = datetime.strptime(date_str, "%d-%m-%y %H:%M:%S")


print(birthday.year)

print(birthday.month)
print(birthday.day)

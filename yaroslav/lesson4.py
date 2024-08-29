# STRING
# format()
# f-strings
# capitalize(), upper(), lower(), title()
# count()
# split()
# join()
# replace()
# startswith(), endswith()
# find(), index()


# st = "{}, {}, {}".format("Hello", "Yaroslav", "How you doing?")
# print(st)
# var_1 = 123
# var_2 = 456
# print(f"{var_1}, {var_2}")

# print(len("heLLo DASDsd"))
# print("asd, qwe, asd".split('a'))
# print("asd".join(["asd", "qwe"]))
# print("asd".replace("s", "F"))
# print("asd".endswith("d"))
# print("ads".find("d"))
# print("qweasd".index("a"))

# "Hello i want to invite Yarosalv Sidoruk to my birthday!!!"

# list_of_names = [
#     "Dzina", "Masha", "Nastya", "Anton", "Anna",
#     "Andrey", "Arina", "Elena", "Roman","Gleb",
#     "Lev", "Nikolay", "Polina", "Yrua", "Anton"
# ]
# for name in list_of_names:
#     print(f"hello i want to invite {name} to my birthday!!!".capitalize())


# LIST
# Объединение
# Повторение
# Проверка длины - len()
# Проверка наличия
# insert(), append(), extend()
# Индексация и присваивание - [::] (все индексы начинаются с 0)
# del, remove()
# reverse()
# Сортировка
# max(), min(), sum()

example_list = ["Dzina", "Masha", "Nastya", "Anton", "Anna",]
example_list1 = [0,12,1, 12, 2, 12, 3, 12, 2,3,4]
# list3 = example_list + example_list1
# list4 = example_list1 * 3
# print(example_list1 * 3)
# print(len(example_list1 * 3))
# example_list1.insert(1, 12)
# print(example_list1)
# example_list1.append("asd")
# print(example_list1)
# example_list1.extend(example_list)
print(example_list1[-2:])
# print(example_list1)

# del example_list1[1]
example_list1.remove(12)
print(example_list1)
example_list1.remove(12)
print(example_list1)
for i in range(len(example_list1)):
    if 12 in example_list1:
        example_list1.remove(12)
        print(example_list1)
    else:
        print("no 12 in exampl list")
        break

# last_element = example_list1.pop()
# print(last_element)
# last_element = example_list1.pop()
# print(last_element)
# example_list1.remove(12)
# print(example_list1)
# example_list1.reverse()
# print(example_list1)
# print(sorted(example_list1))
# print(sum(example_list1))


# dict
# Распаковка другого словаря - **
# Добавление элементов
# Удаление элементов
# Объединение словарей
# items()
# values()
# keys()
# Counter - подсчет количества элементов в словаре

# SET
# Добавление и удаление элементов
# len()
# Объединение
# Пересечение
# Множество из элементов, встречающихся в одном множестве, но не
# встречающиеся в обоих.

print("Yaroslav, Hello world!")
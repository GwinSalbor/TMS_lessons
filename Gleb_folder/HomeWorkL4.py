### Задание 1-2

# print("Робот: Напишите сообщение")
# human = input("Человек: ").lower()
# if human == "привет":
#     print("Робот: Привет, человек! Как ты?")
# elif human =="хай":
#     print("Робот: Васап, мэн! Как ты?")
# else:
#     print("Робот: Ты мне втираешь какую-то дичь. Но это уже совсем другая история. Как ты?")

# human = input("Человек: ").lower()
# if human.startswith("хорошо"):
#     print("Робот: Я машина, у меня нет эмоций. Чем ты интересуешься?")
# elif human == "не очень":
#     print("Робот: Та ты не расстраивайся, у меня эмоций вообще нет. Чем ты интересуешься?")
# else:
#     print("Робот: Я шучу. Мне не интересно. Чем ты интересуешься?")

# human = input("Человек: ").lower()
# if human == "искусством":
#     print("Робот: Мне очень интересно искусство кожанных. давай поговорим о нём.")
# else:
#     print("Робот: Это очень занимательно. но я больше увлекаюсь вашим искусством")

# human = input("Человек: ").lower()
# if human.startswith("робот сочинит"):
#     print("Робот: А вы?")

# human = input("Человек: ").lower()
# if human.startswith("робот превратит"):
#     print("Робот: А н@гр мне тут может не сидеть и рэп не исполнять.")
#     print("Робот: Ты, тумба юмба. Едь в свой Эквадор и сиди бананы жуй.")

### Задание 3
# str1 = ("Robin Singh")
# list = str1.split( )
# print(list)

# str2 = ("I love arrays they are my favorite")
# list = str2.split( )
# print(list)

### Задание 4
# name = ['Ivan', 'Ivanou']
# country = ("Belarus")
# city = ("Minsk")
# print(f"Привет, {name[0]} {name[1]}! Добро пожаловать в {city} {country}")

### Задание 5
# word_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
# print(" ".join(word_list))

### Задание 6
# num_list = [2, 4, 8, 6, 89, 6, 7, 3, 5, 10]
# val = 67
# num_list.insert(2, val)
# print(num_list)

# num_list.pop(3)
# print(num_list)

### Задание 7
# el_list = []
# for i in range(10):
#     inp = input()
#     el_list.append(inp)
# el_list = sorted(el_list)
# print(el_list)

### Доп. задание 1
# num_list1 = [1, 5, 2, 9, 9, 2, 1]
# for unique_number in num_list1:
#     number_count = num_list1.count(unique_number)
#     if number_count == 1:
#         print(unique_number)

# ### Доп. задание 2
text = """I like to be at home. It is my happy place. It is a place where my family gets together.
We live in a two-storey house. Our living room is on the ground floor. 
There we sit, watch movies and play games. 
My little sister likes to play with her dolls there. 
I often find her toys under the tabletttttttt."""
max_count = []
dct = {}
text1 = sorted(text.lower())
for letter in text1:
    if letter.isalpha():
        dct[letter] = text1.count(letter)
for letter in dct:
    if dct[letter] == max(dct.values()):
        max_count.append(letter)

print(" ".join(max_count))



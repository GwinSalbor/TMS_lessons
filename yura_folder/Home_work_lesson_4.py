# Задание 1-2
user_ansver = input("Вы: ").lower()

if user_ansver == "привет":
    print("Бот: Привет! Как твои дела?")
elif user_ansver.startswith("здравствуй"):
    print("Бот: Здравствуйте! Как ваши дела?")
elif user_ansver.startswith("добрый день"):
    print("Бот: Добрый день! Как ваши дела?")
else:
    print("Бот: Я тебя не понимаю. Попробуй начать с 'Привет' или подобного приветствия.")

user_ansver = input("Вы: ").lower()

if user_ansver == "хорошо":
    print("Бот: Это супер! Сегодня отличный день!")
elif user_ansver == "плохо":
    print("Бот: Я могу рассказать тебе анекдот?")

    user_ansver = input("Вы: ").lower()
    if user_ansver == "да":
        print("Бот: Колобок повесился.")
    elif user_ansver == "нет":
        print("Бот: Тогда тебе стоит выпить чаю и отдохнуть.")
else:
    print("Бот: Я тебя не понимаю.")

# Задание 3

string1 = "Robin Singh"
string2 = "I love arrays they are my favorite"

list1 = string1.split()
list2 = string2.split()

print(list1)
print(list2)

# Задание 4 

name_list = ['Ivan', 'Ivanou']
city = "Minsk"
country = "Belarus"

output = f"Привет, {name_list[0]} {name_list[1]}! Добро пожаловать в {city} {country}"
print(output)

# Задание 5
 
words_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]

result_string = " ".join(words_list)

print(result_string)

# Задание 6

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Вставка нового значения на 3-ю позицию
new_value = 200
my_list.insert(2, new_value)

# Удаление элемента
index_to_remove = 8
if 0 <= index_to_remove < len(my_list):
    del my_list[index_to_remove]

print(my_list)

# Задание 7 

user_list = []

# Шаг 2: Наполнение списка элементами из консоли
for i in range(10):
    element = input(f"Введите элемент {i+1}: ")
    user_list.append(element)

# Шаг 3: Сортировка списка
user_list.sort()

print(user_list)
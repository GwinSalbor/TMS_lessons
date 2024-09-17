# # #1.1-1.2
# # user = input().lower()
# # if user == "привет":
# #     print("Bot: Привет! Как твое настроение?")
# # elif user.startswith("hello"):
# #     print("Bot: Hi! How are you?")
# # elif user.startswith("hejka"):
# #     print("Bot: Czesc! Jak sie masz?")
# # else:
# #     print("command not found")
# #
# # user = input().lower()
# # if user == "хорошо":
# #     print("Bot: Отлично! Сегодня хороший день!")
# # elif user == "плохо":
# #     print("Bot: Хочешь развлечься?")
# #
# #     user = input().lower()
# #     if user == "да":
# #         print("Bot: Отлично! Я подберу список событий в твоем городе!")
# #     elif user == "нет":
# #         print("Bot: Я бы рекомендовал отдохнуть!")
# # else:
# #     print("command not found")
#
# #1.3
#
# str1 = "Hi, my name Piter Parker."
# list = str1.split()
# print(list)
#
# #1.4
#
# name_list = ['Ivan', 'Ivanov']
# str2 = 'Minsk'
# str3 = 'Belarus'
# print(f'Привет, {name_list[0]} {name_list[1]}! Добро пожаловать в {str2} {str3}')
#
# #1.5
# list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
# print(' '.join(list))
#
# #1.6
#
# list=[1,2,3,4,5,6,7,8,9,10]
# list.insert(2, 100)
# print (list)
# list.pop(2)
# print(list)

#1.7

my_list = []
for i in range(0,10):
    i = input()
    my_list.append(i)
print(sorted(my_list))
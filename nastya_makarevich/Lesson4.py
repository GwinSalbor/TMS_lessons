# list_of_names = [
#     "Dzina", "Masha", "Nastya", "Anton", "Anna",
#     "Andrey", "Arina", "Elena", "Roman","Gleb",
#     "Lev", "Nikolay", "Polina", "Yrua", "Anton"
# ]
# for name in list_of_names:
#     print(f"Hello i want to invite {name} to my birthday!")

summ = 0
a = input()
for i in a:
    if i.isdigit():
        print("цифра ", 1)
        var = int(i)
        summ += var
    else:
        print("это буква", i)
print(summ)





# "Hello Piotr!! Where is my money?"
# list_of_names = [
#     "Dzina", "Masha", "Nastya", "Anton", "Anna",
#     "Andrey", "Arina", "Elena", "Roman","Gleb",
#     "Lev", "Nikolay", "Polina", "Yrua", "Anton"
# ]
# for name in list_of_names:
#     print(f"Hello {name}!! Where is my money?")

summ=0
a = input()
for i in a:
    if i.isdigit():
        print("number", i)
        var = int(i)
        summ += var
    else:
        print("lit", i)
print(summ)
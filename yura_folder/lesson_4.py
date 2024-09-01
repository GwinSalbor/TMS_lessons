a = input()
list_for_numbers = []

for i in a:
    if i.isdigit():
        list_for_numbers.append(int(i))

print(sum(list_for_numbers))




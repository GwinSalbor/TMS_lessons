"""
Создать три переменные, содержащие возраст трех ближайших соседей, найти сумму и вывести ее на экран.
Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран.

"""

neighbour_1 = 20
neighbour_2 = 88
neighbour_3 = 34

total = neighbour_1 + neighbour_2 + neighbour_3
av_age = total // 3

print(f'The total age number is {total} and the average age is equal to {av_age}')
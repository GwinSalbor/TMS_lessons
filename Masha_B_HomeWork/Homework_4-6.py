"""
Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
удалите элемент из списка под индексом.
"""

my_list = ['Sims 4', 'Resident Evil', 'Outlast', 'Silent Hill', 'Fear', 'Far Cry', 'Visage', 'The Evil Within',
           'Final Fantasy', 'Need For Speed']
my_list.insert(2, 'GTA')
removed_game = my_list.pop(9)
print(my_list, 'Removed game: ', removed_game)
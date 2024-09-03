"""
В цикле на 10 элементов, наполняйте список элементами из консоли, потом отсортируйте этот список.
"""

makeup_bag = []

for i in range(10):
    new_makeup = input("Add makeup to your make-up bag: ").lower()
    makeup_bag.append(new_makeup)

makeup_bag.sort()
print(f"Your make-up bag includes {makeup_bag}")


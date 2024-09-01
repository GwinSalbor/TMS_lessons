num1 = False
num2 = True
num3 = 14

def logic_and(num1, num2):
    print("and: ", bool(num1 and num2))
def logic_or(num1, num2):
    print("or: ", bool(num1 or num2))
def logic_xor(num1, num2):
    print("xor: ", bool(num1 ^ num2))
logic_and(num1, num2)
logic_or(num1, num2)
logic_xor(num1, num2)


a = 20
b = 40
if a > b:
    print("a")
else:
    print("b")


a = 20
b = 40
if a > b:
    print("a")
elif a == 20:
    print(20)
else:
    print("b")



for i in range(1, 10):
    if i == 5:
        print("five")
    elif i % 2 == 1:
        print("odd")
    else:
       print(i)





first_list = [1, 2, 3]
first_set = {1, 2, 3}
first_dict = {"key": 1, 4:"asd"}

print(first_dict["key"])

for i in first_list:
    print(i)

for i in first_dict:
    print(i)
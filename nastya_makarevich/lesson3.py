num1 = False
num2 = True
num3 = 8
def logic_and(num1, num2):
    print("and: " ,bool(num1 and num2))
def logic_or(num1, num2):
    print("or: " ,bool(num1 or num2))
def logic_xor(num1, num2):
    print("xor: " ,bool(num1 ^ num2))
logic_and(num1, num2)
logic_or(num1, num2)
logic_xor(num1, num2)


number = 12
number1 = 23
if number>number1:
    print("number")
else:
    print("number1")



for i in range(1, 10):
    if i == 5:
        print("five")
    elif i % 2 == 1:
        print("odd")
    else:
        print(i)



first_list = [1, 2, 3]
first_set = {3, 5, 6}
first_dict = {"key": 1, 4: "asd"}
print(first_dict["key"])

# for i in first_list:
#     print(i)

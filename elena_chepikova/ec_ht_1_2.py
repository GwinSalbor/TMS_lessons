# 1.a Create variables for all data types we have studied

a1 = 10 # int
a2 = 3.14 # float
a3 = "Hello world!" # string
a4 = True # boolean

print("1.a:")
print(type(a1), a1)
print(type(a2), a2)
print(type(a3), a3)
print(type(a4), a4)

# 1.b Use operators (+,-,*,/,**) for int and float variables
b1 = a1 + a2 # sum
b2 = a1 - a2 # substr
b3 = a1 * a2 # multiplication
b4 = a1 / a2 # division
b5 = a2 ** a1 # exp

print("1.b:")
print("b1 = a1 + a2 = ", b1)
print("b2 = a1 - a2 = ", b2)
print("b3 = a1 * a2 = ", b3)
print("b4 = a1 / a2 = ", b4)
print("b5 = a2 ** a1 = ", b5)

# 1.c Set variables as a grocery list items and check the total sum
apples = 6.79
bread = 4.99
milk = 3.49
pasta = 5.89
coffee = 24.99

check = apples + bread + milk + pasta + coffee

print("1.c: Total sum of the check: ", check)

# 1.d Set 3 int variables: first variable = int, second - first variable + 3, third - sum of variable 1 and variable 2
d1 = 15
d2 = d1 + 3
d3 = d1 + d2

print("1.d: ", d1, d2, d3)

# 1.e Set string variables and combine them
product1 = "apples"
product2 = "bread"
product3 = "milk"

print(f"1.e: I have: {product1}, {product2}, {product3}.")
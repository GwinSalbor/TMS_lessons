import numpy as np
import random
import string
from datetime import datetime
import os

# Functions and arguments. Task 1.

def calculate(a, b, action):
   """
    This function calculates the sum / the subtraction / the multiplication / the division of two entered digits based on the selected operator.
   :param a: int, float
   :param b: int, float
   :param action: str: valid options: "+", "-", "*", "/"
   :return: str
   """
   def add(a, b):
       print(f"Result: {a} + {b} =", a + b)
   def sub(a, b):
       print(f"Result: {a} - {b} =", a - b)
   def mult(a, b):
       print(f"Result: {a} * {b} =", a * b)
   def div(a, b):
       print(f"Result: {a} / {b} =", a / b)

   actions = {"+": add, "-": sub, "*": mult, "/": div}

   if action in actions:
        return actions[action](a, b)
   else:
        print("Invalid action is selected. Use one of the following actions: +, -, *, /.")


calculate(1, 5, action = "+")
calculate(1, 5, "-")
calculate(1, 5, "*")
calculate(1, 5, "/")
calculate(1, 5, "asd")

# Functions and arguments. Task 2.

def calculate_statistics(*args, stat):
    """
    This function calculates the average / the minumum value / the maximum value / the sum / the median of the provided number list
    :param args: int, float
    :param stat: str, one of the following: "avg", "min", "max", "sum", "med",
    :return: float, int, str
    """
    if stat == "avg":
        return np.average(args)
    elif stat == "min":
        return np.min(args)
    elif stat == "max":
        return np.max(args)
    elif stat == "sum":
        return sum(args)
    elif stat == "med":
        return np.median(args)
    else:
        return ("Invalid statistics type is selected. Please use one of the following: "
                "avg - for average; min - for minimum; max - for maximum; sum - for sum; med - for median")

print(calculate_statistics(1,2,3,4,5,6,7, stat = "avg"))
print(calculate_statistics(1,2,3,4,5,6,7, stat = "sum"))
print(calculate_statistics(1,2,3,4,5,6,7, stat = "min"))
print(calculate_statistics(1,2,3,4,5,6,7, stat = "max"))
print(calculate_statistics(1,2,3,4,5,6,7, stat = "med"))
print(calculate_statistics(1,2,3,4,5,6,7, stat = "asd"))

# Files Handling. Task 1.

def str_generator():
    """
    This function generates random string containing 100 symbols (letters and digits) to be used in add_line_to_file() function.
    :return: str
    """
    seq = list(string.ascii_letters + string.digits)
    line = "".join(random.choices(seq, k=100))
    return line

def code_generator():
    """
    This function randomly selects one of the codes [200, 300, 400, 500] based on weights [2,1,1,1] to be used in add_line_to_file() function.
    :return:
    """
    codes = [200, 300, 400, 500]
    code = random.choices(codes, weights=[2,1,1,1], k=1)
    return str(code[0])

def add_lines_to_file():
    current_date = datetime.now()

    with open('all_codes.txt', "w") as file:
        for i in range(5):
            file.write(f"{current_date} {str_generator()} {code_generator()}\n")
    print("File created and updated successfully")

add_lines_to_file()

# Files Handling. Task 2.
def split_file_by_code():
    """
    This function looks through the file created by add_lines_to_file() function, creates files:
    200_code.txt, 300_code.txt, 400_code.txt, 500_code.txt
    and fills them up based on the value of the code at the end of the line
    """
    if not os.path.exists("all_codes.txt"):
        print("The file does not exist")
    else:
        file = open('all_codes.txt', "r")
        file1 = open('200_code.txt', "w")
        file2 = open('300_code.txt', "w")
        file3 = open('400_code.txt', "w")
        file4 = open('500_code.txt', "w")
        for line in file:
            if line.endswith("200\n"):
                file1.write(line)
            elif line.endswith("300\n"):
                file2.write(line)
            elif line.endswith("400\n"):
                file3.write(line)
            elif line.endswith("500\n"):
                file4.write(line)
            else:
                print(f"Code is not detected in line: {line}")
        file.close()
        file1.close()
        file2.close()
        file3.close()
        file4.close()

split_file_by_code()
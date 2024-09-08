#region 1.1

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

def calculate(a, b, operation):
    if operation == '+':
        return add(a, b)
    elif operation == '-':
        return sub(a, b)
    elif operation == '*':
        return mult(a, b)
    elif operation == '/':
        return div(a, b)
    else:
        return "Invalid operation"

#endregion

#region 1.2

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"


def calculate(a, b, operation):
    operations = {
        '+': add,
        '-': sub,
        '*': mult,
        '/': div
    }

    if operation in operations:
        return operations[operation](a, b)
    else:
        return "Invalid operation"
#endregion

#region 2

def calculate_statistics(*args, stat):
    if not args:
        return "No numbers provided"

    if stat == 'avg':
        return sum(args) / len(args)
    elif stat == 'max':
        return max(args)
    elif stat == 'min':
        return min(args)
    elif stat == 'sum':
        return sum(args)
    else:
        return "Invalid statistic"

#endregion

#region 3

import random
import string

def generate_random_string(length=10):

    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def write_strings_to_file(filename, num_strings=5):

    numbers_to_append = [100, 200, 300, 400, 500]

    with open(filename, 'w') as file:
        for _ in range(num_strings):
            random_string = generate_random_string()
            for number in numbers_to_append:
                file.write(f"{random_string}{number}\n")


write_strings_to_file('random_strings.txt')

#endregion

#region 3.1

import random
import string
from datetime import datetime


def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def write_strings_to_file(filename, num_strings=5):
    numbers_to_append = [100, 200, 300, 400, 500]

    with open(filename, 'w') as file:
        for _ in range(num_strings):
            random_string = generate_random_string()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for number in numbers_to_append:
                file.write(f"{current_time} {random_string}{number}\n")


write_strings_to_file('random_strings.txt')

#endregion

#region 3.2

import random
import string
from datetime import datetime

def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def write_strings_to_file(filename, num_strings=5):
    numbers_to_append = [100, 200, 300, 400, 500]

    with open(filename, 'w') as file:
        for _ in range(num_strings):
            random_string = generate_random_string()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for number in numbers_to_append:
                file.write(f"{current_time} {random_string}{number}\n")

def split_file_by_status(input_filename):
    status_files = {
        200: open('status_200.txt', 'w'),
        300: open('status_300.txt', 'w'),
        400: open('status_400.txt', 'w'),
        500: open('status_500.txt', 'w')
    }

    with open(input_filename, 'r') as file:
        for line in file:
            status = int(line.strip()[-3:])
            if status in status_files:
                status_files[status].write(line)

    for file in status_files.values():
        file.close()


write_strings_to_file('random_strings.txt')
split_file_by_status('random_strings.txt')

#endregion
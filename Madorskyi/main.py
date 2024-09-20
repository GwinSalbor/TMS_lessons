#region HW 1

# linear function: factorial
def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# generator function: factorial_gen
def factorial_gen(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
        yield result


# recursive function: factorial_recursive
def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)



import timeit

n = 10

linear_time = timeit.timeit(lambda: factorial(n), number=1000)
print(f"Linear factorial time: {linear_time} seconds")

generator_time = timeit.timeit(lambda: list(factorial_gen(n))[-1], number=1000)
print(f"Generator factorial time: {generator_time} seconds")

recursive_time = timeit.timeit(lambda: factorial_recursive(n), number=1000)
print(f"Recursive factorial time: {recursive_time} seconds")

#endregion

#region HW 2

def typed(type='str'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if type == 'str':
                new_args = [str(arg) for arg in args]
                new_kwargs = {k: str(v) for k, v in kwargs.items()}
            else:
                new_args = args
                new_kwargs = kwargs
            return func(*new_args, **new_kwargs)
        return wrapper
    return decorator

@typed(type='str')
def add_two_symbol(a, b):
    return a + b


def typed(type='int'):
    def decorator(func):
        def wrapper(*args):
            cast_type = None
            if type == 'int':
                cast_type = int
            elif type == 'float':
                cast_type = float
            else:
                raise ValueError(f"Unsupported type: {type}")

            converted_args = [cast_type(arg) for arg in args]
            return func(sum(converted_args))

        return wrapper

    return decorator


@typed(type='int')
def add_three_symbol(sum_value):
    return sum_value

#endregion

#region HW 3

number_words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

def sort_numbers_lexicographically(numbers):
    numbers_list = list(map(int, numbers.split()))
    numbers_list.sort(key=lambda x: number_words[x])
    return ' '.join(map(str, numbers_list))


input_numbers = "1 2 3"
sorted_numbers = sort_numbers_lexicographically(input_numbers)
print(sorted_numbers)

#endregion
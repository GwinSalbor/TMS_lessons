"""
Напишите функцию calculate_statistic, которая принимает на вход список чисел и возвращает среднее значение, 
максимальное значение, минимальное значение сумму и тд (можете что-то придумать сами не обязательно но будет полезно).
Реализуйте обработку произвольного числа аргументов с помощью *args и поддержите именованные параметры с помощью 
**kwargs, чтобы можно было задавать настройки поиска значения. 
Пример вызова:
    calculate_statistic(1,2,3,4,5,6,7, stat=”avg”) - вернет среднее значение введенных чисел и это 4
    calculate_statistic(1,2,3,4,5,6,7, stat=”sum”) - вернет сумму 28

"""

def sum(values: int) -> int:

    """
    Вычисляет и возвращает сумму принимаемых на вход int чисел
    """

    values_of_sum: int = 0

    for i in values:
        values_of_sum += i

    return values_of_sum


def avg(values: int) -> float:

    """
    Вычисляет и возвращает среднее значение int чисел, принимаемых на вход
    """

    values_of_avg: int = 0

    quantity_of_values: int = 0

    for i in values:
        values_of_avg += i
        quantity_of_values += 1

    return values_of_avg / quantity_of_values



def min(values: int) -> int:

    """
    Считает минимальное значение из int чисел, принимаемых на вход
    """

    value_counter: int = values[0]
    
    for i in values:
        if i < value_counter:
            value_counter = i

    return value_counter


def max(values: int) -> int:

    """
    Считает максимальное значение из int чисел, принимаемых на вход
    """

    value_counter: int = values[0]
    
    for i in values:
        if i >= value_counter:
            value_counter = i

    return value_counter


def calculate_statistic(*args: int, **kwargs: dict):

    """
    Принимает на вход int числа и dict словарь, состоящий из {stat : "вызов действия"}.
    Возвращает результат функций sum, avg, min, max
    """

    values_of_choise: str = kwargs.get(''.join(list(kwargs.keys())))

    match values_of_choise:
        case "sum":
            return sum(args)
        case "avg":
            return avg(args)
        case "min":
            return min(args)
        case "max":
            return max(args)
        

print(calculate_statistic(49,70,50,67,197,56,76,129,1153, stat="max"))
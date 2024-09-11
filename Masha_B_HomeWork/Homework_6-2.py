"""
Напишите функцию calculate_statistic, которая принимает на вход список чисел и возвращает среднее значение,
максимальное значение, минимальное значение сумму и тд
(можете что-то придумать сами не обязательно но будет полезно).
Реализуйте обработку произвольного числа аргументов с помощью *args
и поддержите именованные параметры с помощью **kwargs, чтобы можно было задавать настройки поиска значения.
Пример вызова:
calculate_statistic(1,2,3,4,5,6,7, stat=”avg”) - вернет среднее значение введенных чисел и это 4
calculate_statistic(1,2,3,4,5,6,7, stat=”sum”) - вернет сумму 28
"""


def calculate_statistics(*args, **kwargs):
    stat = kwargs.get('stat')

    if stat == 'sum':
        return sum(args)
    elif stat == 'avg':
        return sum(args) // len(args)
    elif stat == 'max':
        return max(args)
    elif stat == 'min':
        return min(args)
    else:
        return 'incorrect value'


print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='sum'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='avg'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='max'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='min'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='blablabla'))
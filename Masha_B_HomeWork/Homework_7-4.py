"""
Необходимо составить список чисел, которые указывают на длину слов в строке:
sentence = "the quick brown fox jumps over the lazy dog",
но только если слово не "the", с обработкой исключений.
"""

sentence = "the quick brown fox jumps over the lazy dog"


def my_func():
    new_list = sentence.split()
    for i in new_list:
        try:
            if i == 'the':
                raise ValueError('Contains THE')
            else:
                yield len(i)

        except ValueError:
            pass


updated_list = list(my_func())
print(updated_list)


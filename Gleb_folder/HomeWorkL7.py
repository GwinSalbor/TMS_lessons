# ###Задание 1.1
# print((lambda  name: f'Hello, {name}') ('Gleb'))

# # ###Задание 1.2
# from typing import Callable
# names: list[str] = ["Andrei", "Masha", "Lev", "Polina"]
# greet_list: Callable[[list[str]], str] = lambda names: "\n".join([f'Hello, {name}' for name in names])
# print(greet_list(names))

# # ###Задание 2.1

# numbers: list[float] = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# def generator(numbers: list[float]) -> 'generator[float, None, None]':
#     """Принимает список чисел с плавающей точкой и возвращает объект генератора, который будет генерировать положительные числа

#     Args:
#         numbers (list[float]): Cписок чисел с плавающей точкой.


#     Yields:
#         Возвращает положительные числа из списка
#     """
#     for i in numbers:
#          if i > 0:
#              yield i
             
# positive_numbers = generator(numbers)
# print(list(positive_numbers))

# # ###Задание 2.2
# sentence: str = "the quick brown fox jumps over the lazy dog"

# def word_lengths(sentence: str) -> list[int]:
#     """Вычисляет длину всех слов в тексте (за исключением the) и выводит значения в новый список

#     Args:
#         sentence (str): Принимаемый текст

#     Returns:
#         list[int]: Список значений длинн слов
#     """
#     lengths: list[int] = []
#     try:
#         words: list[str] = sentence.split()
        
#         if "the" in words:
#             print('Произошла ошибка: В строке присутствует слово "the"')
        
#         lengths = [len(word) for word in words if word != "the"]
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#     return lengths

# print(word_lengths(sentence))

## Шифр цезаря

from collections import defaultdict
import string

letter_frequency: dict[str, float] = {
    'E': 12.70,
    'T': 9.06,
    'A': 8.17,
    'O': 7.51,
    'I': 6.97,
    'N': 6.75,
    'S': 6.33,
    'H': 6.09,
    'R': 5.99,
    'D': 4.25,
    'L': 4.03,
    'C': 2.78,
    'U': 2.76,
    'M': 2.41,
    'W': 2.36,
    'F': 2.23,
    'G': 2.02,
    'Y': 1.97,
    'P': 1.93,
    'B': 1.49,
    'V': 0.98,
    'K': 0.77,
    'J': 0.15,
    'X': 0.15,
    'Q': 0.10,
    'Z': 0.07
}

# text: str = """some text"""

text: str = """Ot znk hkmottotm, znkxk cgy g sgt cnu qtkc tuznotm ul znk cuxrj gxuatj nos. Noy keky uvktkj zu znk yqe, gtj nk cutjkxkj cngz rge hkeutj znk yzgxy. Znk cotjy cnoyvkxkj ykixkzy, znk xobkxy igxxokj yzuxoky, gtj znk suatzgoty yzuuj gy gtioktz yktzotkry magxjotm znk noyzuxe ul znk kgxzn. Gy znk jgey vgyykj, znk sgt rkgxtkj znk cgey ul znk cuxrj, nuc znk yat xuyk ot znk kgyz gtj ykz ot znk ckyz, nuc znk suut lurruckj ozy vgzn gixuyy znk tomnz yqe, gtj nuc znk ykgyuty ingtmkj. Znk zxkky ynkj znkox rkgbky ot gazast, znk lruckxy hruuskj ot yvxotm, gtj rolk iutzotakj ot g ieirk gy urj gy zosk ozykrl.

Nk cgzinkj znk hoxjy zgqk lromnz, yugxotm ghubk znk rgtj, lxkk zu kdvruxk znk bgyz kdvgtyk ul znk nuxofut. Nk sgxbkrkj gz znk ixkgzaxky ul znk luxkyz, kgin cozn ozy uct atowak xnezns gtj vaxvuyk. Znk curbky nucrkj zu znk suut, znk jkkx mxgfkj ot znk skgjuc, gtj znk yzxkgsy lruckj ktjrkyyre znxuamn znk bgrrkey. Znk sgt lkrz g iuttkizout zu znk cuxrj, gy znuamn nk ckxk g vgxz ul yuskznotm mxkgzkx zngt nosykrl. Nk luatj yurgik ot znk waokz susktzy, cnkt znk cotj hxaynkj gmgotyz noy yqot gtj znk yat cgxskj noy lgik. Nk royzktkj zu znk yuatjy ul znk kgxzn, znk xayzrotm ul rkgbky, znk inoxvotm ul otykizy, gtj znk joyzgtz igrr ul gt ucr.

Zosk subkj luxcgxj, gtj znk sgt mxkc urjkx, haz noy cutjkx tkbkx lgjkj. Nk iutzotakj zu kdvruxk, zu ykkq uaz tkc nuxofuty, gtj zu rkgxt lxus znk cuxrj gxuatj nos. Cozn kgin vgyyotm jge, nk atjkxyzuuj g rozzrk suxk ghuaz znk seyzkxoky ul rolk, haz nk gryu xkgrofkj zngz yusk znotmy cuarj luxkbkx xksgot hkeutj noy mxgyv. Znk yzgxy, znk yqe, znk atobkxyk — grr ul oz yzxkzinkj uaz hkluxk nos, bgyz gtj otlotozk, gtj ekz, nk qtkc zngz nk cgy haz g ysgrr vgxz ul g sain rgxmkx cnurk."""

mode: str = input("Введите encode для шифрования или decode для дешифрования): ")
shift = str = input("Введите сдвиг (для encode обязательно! Для decode - если сдвиг неизвестен, то не вводите ничего): ")

cracker_letters_frequency: defaultdict [str: int] = defaultdict(int)
def cracker(text: str) -> tuple[int, float]:
    """Функция для автоматического нахождения сдвига в тексте

    Args:
        text (str): Принимает зашифрованный текст

    Returns:
        tuple[int, float]: Возвращает найденный сдвиг
    """
    real_len: int = 0
    for i in text:
        if i in string.ascii_letters:
            real_len+=1
            cracker_letters_frequency[i] += 1
    max: float = 0
    expected_e: str = ""
    for letter, frequency in cracker_letters_frequency.items():
        temp: float = frequency / real_len 
        cracker_letters_frequency[letter] = temp
        if max < temp:
            max = temp
            expected_e = letter
    shift: int = ord(expected_e) - ord("e")
    return shift, max

def caesar_cipher(text: str, shift: int, mode: str = 'encode') -> str:
    """Функция в которой описана логика шифра Цезаря для encode и decode

    Args:
        text (str): Переменная в которой указывается текст для шифровки или дешифровки
        shift (int): Сдвиг на который смещены буквы в тексте
        mode (str, optional): Выбор режима работы (encode - для шифрования, decode - для дешифровки).
Returns:
        str: Возвращает зашифрованный или расшированный текст (в зависимости от выбранного режима)
    """
    if mode == 'decode':
        shift = -shift
    
    result: list[str] = [] 
    
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char: str = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)  

    return ''.join(result) 

# Проверяем режим и обрабатываем ввод сдвига
if mode == 'decode' and not shift:
    # Если режим decode и сдвиг не введён, вычисляем сдвиг с помощью функции cracker
    shift, _ = cracker(text)
    print(f"Вычисленный сдвиг: {shift}")
elif shift:
    # Преобразуем введённый сдвиг в int, если он введён
    try:
        shift = int(shift)
    except ValueError:
        print("Ошибка: введённое значение сдвига не является числом!")
        exit()
else:
    # Если сдвиг не введён в режиме encode, завершаем программу
    print("Ошибка: для режима 'encode' необходимо ввести сдвиг!")
    exit()
    
res: str = caesar_cipher(text, shift, mode)

print(f"Результат: {res}")
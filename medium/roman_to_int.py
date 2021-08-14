# -*- coding: utf-8 -*-

"""
Нужно написать код, который будет переводить римские
символы в привычную нам десятичную систему
(про символы можно почитать тут
https://en.wikipedia.org/wiki/Roman_numerals).

Пример:

roman_to_int('XXI') -> 21
roman_to_int('IV') -> 4
roman_to_int('I') -> 1
roman_to_int('MMXXI') -> 2021
roman_to_int('LDVLIV') -> 499
"""

nbrs = {'M': 1_000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

def roman_to_int(s: str) -> int:
    '''Переводит римские цифры в арабские.'''
    # Результат.
    res = 0
    # Функция получения значения для римской цифры.
    getn = lambda x: nbrs.get(x, 0)

    # Проход по строке с римским числов, не включая последний символ.
    for index, item in enumerate(s[:-1]):
            # Если число больше или равно следующего, тогда число прибавляется
            # к результату, иначе - вычитается.
            res += getn(item) if getn(item) >= getn(s[index + 1]) else -getn(item)

    # К результату прибавляется последнее число в строке с римскими цифрами.
    return res + getn(s[-1])

def roman2int(s: str) -> int:
    '''Рекурсивно переводит римские цифры в арабские.'''
    # Функция получения значения для римской цифры.
    getn = lambda x: nbrs.get(x, 0)

    # Условие завершения рекурсии.
    if len(s) <= 1: return getn(s[:1])

    # Определяет положительное или отрицательное число.
    check_neg = -1 + 2 * (getn(s[0]) >= getn(s[1]))
    # Получение числа для текущей римской цифры
    # и рекурсивный вызов функции для оставшейся строки.
    return check_neg * getn(s[0]) + roman2int(s[1:])



tests = (('XXI', 21), ('IV', 4), ('I', 1), ('MMXXI', 2021), ('LDVLIV', 499))

print('Тесты итерационной функции:')
for s, check in tests:
    print(roman_to_int(s=s) == check)

print('\nТесты рекурсивной функции:')
for s, check in tests:
    print(roman2int(s=s) == check)
    

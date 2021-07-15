# -*- coding: utf-8 -*-

"""
Ваша цель — написать функцию,
которая находит недостающие буквы английского алфавита.

На вход идут только символы английского языка в нижнем регистре.
Возвращаемое значение — строка из недостающих символов.

Пример:

findmissingletters('abc') -> defghijklmnopqrstuvwxyz
findmissingletters('mnopqrstuvwxyz') -> abcdefghijkl
findmissingletters('acegikmoqsuwy') -> bdfhjlnprtvxz

Усложнение: строка может принимать символы в верхнем и
нижнем регистре, а также они могу повторяться.
"""

def findmissingletters(string: str) -> str:
    '''
    Возвращает строку с отсутствующими буквами английского алфавита
    в строке s.
    '''
    check_line = 'abcdefghijklmnopqrstuvwxyz'
    liters = set(string.lower())
    return ''.join(sym for sym in check_line if sym not in liters)



lines = (('abc', 'defghijklmnopqrstuvwxyz'),
         ('mnopqrstuvwxyz', 'abcdefghijkl'),
         ('acegikmoqsuwy', 'bdfhjlnprtvxz'))

for s, check in lines:
    print(findmissingletters(string=s) == check)


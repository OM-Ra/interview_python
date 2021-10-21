# -*- coding: utf-8 -*-

"""
Ваша задача — написать функцию, которая будет проверять, является
ли предложение палиндромом. Палиндромом — предложение, которое
читается одинаков слева на право и с права на лево.

Пример:

is_palindrome('A man, a plan, a canal: Panama') -> True
is_palindrome('0P') -> False
is_palindrome('a.') -> True
"""

from string import punctuation

def is_palindrome(string: str) -> bool:
    # Замена всех символов пунктуации на символ пробела.
    string_not_sym = string.translate(str.maketrans(punctuation, ' ' * len(punctuation)))
    # Удаление всех пробелов и перевод строки в нижний регистр.
    string_not_sym = string_not_sym.replace(' ', '').lower()
    # Сравнение полученной строки с развёрнутой строкой и возврат результата.
    return string_not_sym == string_not_sym[::-1]


# Тесты.
tests = (
    ('A man, a plan, a canal: Panama', True),
    ('0P', False),
    ('a.', True)
)

for index, item in enumerate(tests):
    res = is_palindrome(string=item[0])
    assert res == item[1], f'tests:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая проверяет, является ли число простым.
Простые числа — числа, которые делятся нацело только на единицу и на само себя.

Пример:

is_prime_number(1) -> True
is_prime_number(2) -> True
is_prime_number(9) -> False
is_prime_number(117) -> False
is_prime_number(127) -> True
'''

def is_prime_number(nbr: int) -> bool:
    # Подбор числа для деления.
    for item in range(2, int(nbr ** 0.5) + 1):
        # Проверка на остаток.
        if nbr % item == 0:
            return False
    return True


# Тесты.
tests = ((1, True), (2, True), (9, False), (117, False), (127, True))

for index, item in enumerate(tests):
    res = is_prime_number(nbr=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


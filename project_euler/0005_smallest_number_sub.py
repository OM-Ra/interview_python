# -*- coding: utf-8 -*-

'''
2520 - самое маленькое число, которое делится без остатка на все
числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''

from itertools import count

def smallest_number_sub(border: int) -> int:
    '''border - должен быть кратен 10.'''
    # Подбор искомого числа.
    for res in count(2520, 10):
        # Проход по вариантам делителя.
        for divider in range(3, border):
            # Проверка на остаток от деления.
            if res % divider:
                break
        else:
            # Если все делители divider делили число res без остатка.
            return res


# Тесты.
tests = (
    (10, 2520),
    (20, 232792560)
)

for index, item in enumerate(tests):
    res = smallest_number_sub(border=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


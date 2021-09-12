# -*- coding: utf-8 -*-

'''
Написать функцию, которая будет возвращать все числа,
на которые делится аргумент функции. Если же аргумент —
простое число, то возвращаем строку, как на примере.

Пример:

find_divisors(13) -> 13 - простое число
find_divisors(10) -> [2, 5]
find_divisors(12) -> [2, 3, 4, 6]
'''

from typing import List

def find_divisors(nbr: int) -> List[int] or str:
    # Функция для проверки деления числа nbr нацело divisor.
    func = lambda divisor: not (nbr % divisor)
    # Получение списка с числами делящих число nbr нацело.
    res = list(filter(func, range(2, nbr)))
    # По списку res определяется возвращаемый ответ.
    return res if res else f'{nbr} - простое число'


# Тесты.
tests = (
    (13, '13 - простое число'),
    (10, [2, 5]),
    (12, [2, 3, 4, 6]),
    (1, '1 - простое число')
)

for index, item in enumerate(tests):
    res = find_divisors(nbr=item[0])
    assert res == item[1], f'tests:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


# -*- coding: utf-8 -*-

'''
Написать функцию, которая будет принимать список и находить уникальное число.

Пример:

find_unique_value([1, 2, 1, 1]) 2
find_unique_value([2, 3, 3, 3]) 2
find_unique_value([5, 5, 5, 0.5]) 0.5
'''

from typing import List

#* По условию, должно возвращаться только одно
#* уникальное значение, так что, будет возвращаться
#* первое уникальное значение или None. 

def nbr_unicue(arr: List[float]) -> float or None:
    # Проход по элементам списка.
    for item in arr:
        # Проверка на уникальность.
        if arr.count(item) == 1:
            # Возврат уникального значения.
            return item


# Тесты.
tests = (
    ([1, 2, 1, 1], 2),
    ([2, 3, 3, 3], 2),
    ([5, 5, 5, 0.5], 0.5)
)

for index, item in enumerate(tests):
    res = nbr_unicue(item[0])
    assert res == item[1], f'tests:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


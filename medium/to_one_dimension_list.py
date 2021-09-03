# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая переводит
многомерный массив в одномерный.

Пример:

to_one_dimension_list([1, [2, 3, [4, 5], 6]]) -> [1, 2, 3, 4, 5, 6]
to_one_dimension_list([1, 2, 3]) -> [1, 2, 3]
to_one_dimension_list([1, [[3]], 5])  -> [1, 3, 5]
'''

# Итерируемый тип данных.
from typing import Iterable

def to_one_dimension_list(arr: Iterable[Iterable]) -> list:
    # Результирующий список.
    res = list()
    # Проход по каждому элементу итерируемой последовательности arr.
    for item in arr:
        # Проверка: является ли текущий элемент item итерируемым и не строкой.
        if isinstance(item, Iterable) and not isinstance(item, str):
            # Добавление элементов списка полученного рекурсивно
            # в результирующий список res.
            res.extend(to_one_dimension_list(item))
        else:
            # Добавление элемента в результирующий список.
            res.append(item)
    # Возврат результата.
    return res


# Тесты.
tests = (([1, [2, 3, [4, 5], 6]], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, [[3]], 5], [1, 3, 5]))

for index, item in enumerate(tests):
    res = to_one_dimension_list(arr=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


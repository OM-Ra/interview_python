# -*- coding: utf-8 -*-

'''
Написать функцию, которая будет проверять, существует такой
треугольник или нет по этому
https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D1%80%D0%B0%D0%B2%D0%B5%D0%BD%D1%81%D1%82%D0%B2%D0%BE_%D1%82%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B0
правилу. Она принимает список из трёх сторон треугольника. 

Пример:

is_triangle([10, 12, 23]) -> False
is_triangle([0, 0, 0]) -> False
is_triangle([1, 1, 1]) -> True
is_triangle([12, 12, 12]) -> True
'''

from typing import List

def is_triangle(arr: List[float]) -> bool:
    # Сортировка списка.
    arr.sort()
    # Сравнение суммы двух меньших величин с наибольшей и возврат результата.
    return sum(arr[:-1]) > arr[-1]


# Тесты.
tests = (
    ([10, 12, 23], False),
    ([0, 0, 0], False),
    ([1, 1, 1], True),
    ([12, 12, 12], True)
)

for index, item in enumerate(tests):
    res = is_triangle(arr=item[0])
    assert res == item[1], f'tests:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


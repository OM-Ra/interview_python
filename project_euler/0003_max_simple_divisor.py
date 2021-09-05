# -*- coding: utf-8 -*-

'''
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

from math import ceil

CHECK_LIMIT = 1e6

def max_simple_divisor(nbr: int) -> int:
    # При больших числах, можно сделать предположение,
    # что простой делитель будет меньше или равен корню из числа.
    # Число CHECK_LIMIT взято наугад.

    # Для чисел меньше CHECK_LIMIT простой делитель может быть
    # в пределах половины числа.

    # Получение границы поиска простого делителя.
    new_nbr = ceil(nbr ** 0.5) + 1 \
              if nbr > CHECK_LIMIT \
              else ceil(nbr / 2) + 1
    # Результат.
    res = None

    # Проход по вариантам простого делителя.
    for item in range(2, new_nbr):
        # Если item делитель числа nbr.
        if not (nbr % item):
            # Проверка, простое ли число item
            if max_simple_divisor(item) == 1:
                # Сохранение найденного текущего результата.
                res = item

    # Возврат результата. Минимальный простой делитель - это 1.
    return res if res else 1


#
tests = (
    (13_195, 29),
    (600_851_475_143, 6857),
    (10, 5),
    (17, 1),
    (1_000, 5),
    (1_497, 499),
)

for index, item in enumerate(tests):
    res = max_simple_divisor(nbr=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


# -*- coding: utf-8 -*-

'''
Ваша задача — найти суму всех чисел, перемноженных на их индекс.

Пример:

sum_mult_index([1,2,3,4]) -> 20
sum_mult_index([11,22,55,33,44]) -> 407
sum_mult_index([-1, 0, -8, 11]) -> 17
sum_mult_index([0, 0, 0, 0, 0]) -> 0
'''

from typing import List

# Объявление типа переменной
Vector = List[float]

def sum_mult_index(arr: Vector) -> float:
    '''
    Возвращает сумму всех чисел вектора,
    перемноженных на их индекс.

    arr - список содержащий числа (вектор).
    '''
    return sum(index * item for index, item in enumerate(arr))



arrs = (([1,2,3,4], 20),
        ([11,22,55,33,44], 407),
        ([-1, 0, -8, 11], 17),
        ([0, 0, 0, 0, 0], 0))

for arr, check in arrs:
    print(sum_mult_index(arr=arr) == check)


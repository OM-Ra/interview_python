# -*- coding: utf-8 -*-

'''
Напишите функцию для деления числа.
Она должна принимать любое целое число (в т.ч. отрицательное) и
возвращать список из двух половинок этого числа.
Если входящее число нечетное, в списке должно быть большим второе число.

Примеры:
number_split(4)   [2, 2]
number_split(10)  [5, 5]
number_split(11)  [5, 6]
number_split(-9)  [-5, -4]
'''

from typing import List

def number_split(nbr: int) -> List[int]:
    '''
    Возвращает список с двумя числами: [nbr//2, nbr//2 + остаток].
    '''
    res = divmod(nbr, 2)
    return [res[0], res[0] + res[1]]



tests = ((4, [2, 2]),
         (10, [5, 5]),
         (11, [5, 6]),
         (-9, [-5, -4]))

for nbr, check in tests:
    print(number_split(nbr=nbr) == check)


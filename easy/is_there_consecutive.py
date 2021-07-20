# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать список
цифр и проверять, встречается ли заданная цифра
указанное число раз подряд. Функция должна возвращать
True или False. Исходим из того, что все параметры
всегда будут валидными.

Шаблон:

is_there_consecutive([lst], n, times)

- [lst] — список может быть любой длины, цифры идут в произвольном порядке
- n — цифра, которую нужно проверять
- times — сколько раз подряд должна встретиться цифра n

Примеры:

is_there_consecutive([1, 3, 5, 5, 3, 3, 1], 3, 2)  True
is_there_consecutive([1, 2, 3, 4, 5], 1, 1)  True
is_there_consecutive([3], 1, 0)  True
is_there_consecutive([2, 2, 3, 2, 2, 2, 2, 3, 4, 1, 5], 3, 2)  False
is_there_consecutive([5, 5, 5, 5, 5], 5, 7)  False
'''

from typing import List

def is_there_consecutive(arr: List[int], nbr: int, times: int) -> bool:
    '''Определяет встречаетлся ли число nbr в списке arr times раз подряд.'''
    # Проверяет есть ли строка состоящая из числа nbr повторённого times раз
    # в строке созданной из списка arr.
    return str(nbr) * times in ''.join(map(str, arr))



tests = ((([1, 3, 5, 5, 3, 3, 1], 3, 2), True),
         (([1, 2, 3, 4, 5], 1, 1), True),
         (([3], 1, 0), True),
         (([2, 2, 3, 2, 2, 2, 2, 3, 4, 1, 5], 3, 2), False),
         (([5, 5, 5, 5, 5], 5, 7), False))

for args, check in tests:
    print(is_there_consecutive(*args) == check)


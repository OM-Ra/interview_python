# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать число n и проверять,
кратна ли каждая его цифра цифре, стоящей слева от нее.
Верните массив булевых значений результатов проверок.

Примеры:
divisible_by_left(73312)  [False, False, True, False, True]
# слева от 7 нет элемента = False
# 3/7 = False
# 3/3 = True
# 1/3 = False
# 2/1 = True
divisible_by_left(1)  [False]
divisible_by_left(635)  [False, False, False]
 
Примечание: массив всегда будет начинаться с False, поскольку слева от первой цифры ничего нет.
'''

from typing import List

def divisible_by_left(nbr: int) -> List[bool]:
    '''
    Проверяет кратна ли цифра соседней цифре слева у числа nbr.
    Результат по каждой цифре возвращается в виде списка.
    '''
    # Создание списка цифр числа nbr
    arr = list(map(int, str(nbr)))
    # Если индекс элемента больше нуля, тогда проверяется кратность
    # цифры к цифре слева.
    return [item % arr[index - 1] == 0 if index else False
            for index, item in enumerate(arr)]



tests = ((73312, [False, False, True, False, True]),
         (1, [False]),
         (635, [False, False, False]))

for nbr, check in tests:
    print(divisible_by_left(nbr=nbr) == check)


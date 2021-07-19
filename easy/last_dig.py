# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать три числа
(a, b, c) и возвращать True, если последняя цифра
произведения a * b равна последней цифре числа c.

Примеры:

last_dig(25, 21, 125)  True
# 25 * 21 = 525, последняя цифра - 5.
# Последняя цифра 125 - тоже 5.

last_dig(55, 226, 5190)  True
last_dig(12, 215, 2142)  False
'''

def last_dig(nbr1: int, nbr2: int, nbr3: int) -> bool:
    '''
    Проверяет равна ли последняя цифра произведения
    nbr1 * nbr2 последней цифре nbr3.
    '''
    return str(nbr1 * nbr2)[-1] == str(nbr3)[-1]



numbers = (([25, 21, 125], True),
           ([55, 226, 5190], True),
           ([12, 215, 2142], False))

for nbr, check in numbers:
    print(last_dig(*nbr) == check)


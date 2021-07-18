# -*- coding: utf-8 -*-

'''
Задание:
Напишите функцию, которая будет принимать
целое положительное число и определять,
делится ли оно нацело на сумму цифр этого числа.

Примеры:

is_divisible(75) ➞ False
# 7 + 5 = 12
# 75 не делится нацело на 12

is_divisible(171) ➞ True
# 1 + 7 + 1 = 9
# 171 делится на 9 без остатка

is_divisible(481) ➞ True
is_divisible(89) ➞ False
is_divisible(516) ➞ True
is_divisible(200) ➞ True
'''

def is_divisible(nbr: int) -> bool:
    '''Проверяет делится ли число nbr на сумму его цифр.'''
    return not divmod(nbr, sum(map(int, str(nbr))))[1]

numbers = ((75, False), (171, True), (481, True),
           (89, False), (516, True), (200,True))

for nbr, check in numbers:
    print(is_divisible(nbr=nbr) == check)


# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая будет проверять,
делится ли число на два. Стоит отметить, что использовать
операцию / и % нельзя.

На вход будет идти и отрицательное и положительное число

Пример:
is_even(5) # False
is_even(-4) # True
is_even(-3) # False

Подсказка: -1 должно вернуть False, 0 — True
'''

def is_even(nbr: int) -> bool:
    '''Проверяет чётность числа nbr.'''
    return not (nbr & 1)



tests = ((5, False), (-4, True), (-3, False))

for nbr, check in tests:
    print(is_even(nbr=nbr) == check)


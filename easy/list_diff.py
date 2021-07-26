# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая будет
находить отличия между первым и вторым списком.

Пример:

list_diff([], []) -> []
list_diff([], [1, 2]) -> []
list_diff([1, 2], [2]) -> [1]
list_diff([6, 4, 3], [7]) -> [6, 4, 3]
'''

def list_diff(arr1: list, arr2: list) -> list:
    '''
    Находит отличия в списке arr1 от arr2 и возвращает
    отсортированный список.
    '''
    # Находит разность множеств,
    # конвертирует результат в список,
    # сортирует от большего к меньшему.
    return sorted(list(set(arr1) - set(arr2)), reverse=True)



tests = ((([], []), []),
         (([], [1, 2]), []),
         (([1, 2], [2]), [1]),
         (([6, 4, 3], [7]), [6, 4, 3]))

for args, check in tests:
    print(list_diff(*args) == check)


# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая проверит,
все ли значения увеличиваются на один

Пример:
increasing([-1, 0, 1, 2, 3]) -> True
increasing([-1, 0, 1, 3, 4])) -> False
increasing([0, 1]) -> True
increasing([1, 0]) -> False
'''

def increasing(arr: list) -> bool:
    '''
    Функция проверяет, чтобы все элементы списка возрастали
    на еденицу: [x + 0, x + 1, x + 2, ..., x  + n - 1].
    Где n - длина списка.

    Возвращает True если условие соблюдено, и False в противном случае.
    '''
    if arr:
        return all(item1 + 1 == item2 for item1, item2 in zip(arr, arr[1:]))
    return False



arrs = (([-1, 0, 1, 2, 3], True),
        ([-1, 0, 1, 3, 4], False),
        ([0, 1], True),
        ([1, 0], False),
        ([], False),
        ([1, 0, 3], False))

for arr, check in arrs:
    print(increasing(arr=arr) == check)


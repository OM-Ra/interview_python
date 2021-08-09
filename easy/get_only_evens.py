# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать список чисел
и возвращать список, содержащий только четные числа
исходного списка, имеющие к тому же четные индексы.

Примечание: списки начинаются с индекса 0.

Примеры:

get_only_evens([1, 3, 2, 6, 4, 8]) [2, 4]
get_only_evens([0, 1, 2, 3, 4]) [0, 2, 4]
get_only_evens([1, 2, 3, 4, 5]) []
'''

from typing import List

def get_only_evens(arr: List[int]) -> List[int]:
    '''
    Создание списка состоящего из чётных элементов
    списка arr имеющих чётный индекс.
    '''
    return [item
            for item in arr[::2] # Проход по элементам списка имеющих чётный индекс.
            if not item & 1]     # Проверка на чётность.



tests = (([1, 3, 2, 6, 4, 8], [2, 4]),
         ([0, 1, 2, 3, 4], [0, 2, 4]),
         ([1, 2, 3, 4, 5], []))

for arr, check in tests:
    print(get_only_evens(arr=arr) == check)

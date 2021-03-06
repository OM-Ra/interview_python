# -*- coding: utf-8 -*-

'''
Ваша задача — написать код,
который получает словарик типа:
«Имя : [массив оценок]».

Необходимо среди всех значений словаря
найти ученика с максимальным и минимальным
средним баллом, а после — вывести его имя
вместе со средним балом.

Пример:

Вход: {"Mark":[2, 6, 9, 2],
       "Kevin": [11, 8],
       "John":[7, 4, 11, 5, 8],
       "Max": [2, 4, 5]}

Вывод: Kevin: 9.50, Max: 3.67
'''

def average_mark(arr: dict) -> str:
    '''
    Возвращет строку с именами учеников и
    их максимальным и минимальным средним балом.

    arr - словарь с учениками и их оценками.
    '''
    average = lambda item: sum(arr[item]) / len(arr[item])
    names = sorted(arr, key=average)
    return f'{names[-1]}: {average(names[-1]):.2f}, {names[0]}: {average(names[0]):.2f}'



arr = {"Mark":[2, 6, 9, 2],
       "Kevin": [11, 8],
       "John":[7, 4, 11, 5, 8],
       "Max": [2, 4, 5]}

print(average_mark(arr))


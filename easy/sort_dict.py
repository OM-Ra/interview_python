# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая сортирует
словарь по убываю на основе значения.

Пример:

sort_dict({"1": 1, "2": 2, "3": 3}) -> {"3": 3, "2": 2, "1": 1}
sort_dict({"obj": 8, 1: 11, "6": 4}) -> {1: 11, "obj": 8, "6": 4}
'''

def sort_dict(data: dict) -> dict:
    # Сортировка ключей и значений [(key, value)] по значениям в убывающем порядке.
    data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    # Предыдущий результат переводится в словарь.
    return dict(data)


# Тесты
tests = (({"1": 1, "2": 2, "3": 3}, {"3": 3, "2": 2, "1": 1}),
    ({"obj": 8, 1: 11, "6": 4}, {1: 11, "obj": 8, "6": 4}))

for index, item in enumerate(tests):
    res = sort_dict(data=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


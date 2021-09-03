# -*- coding: utf-8 -*-

'''
Напишите, пожалуйста, функцию, которая превращает
одномерный список в список из пар. 

Если количество элементов в списке не позволяет поделить его на 2,
то метод использует необязательный метод fill_char с значением для заполнения.

Желательно не использовать сторонние модули.

Пример:

to_pairs([1, 2, 3, 4]) -> [[1, 2], [3, 4]]
to_pairs([1, 2, 3, 4, 5]) -> [[1, 2], [3, 4], [5, None]]
to_pairs([1, 2, 3, 4, 5, 0], fill_char = 0) -> [[1, 2], [3, 4], [5, 0]]
'''

from typing import List, Any

def to_pairs(arr: List[Any], fill_char: Any =None) -> List[List[Any]]:
    # Возврат результата.
    return [[item1, item2]
            # Проход по каждому второму элементу списка:
            # первый срез: начиная от начала;
            # второй срез: со сдвигом на первый элемент и добавление к срезу fill_char.
            for item1, item2 in zip(arr[::2], arr[1::2] + [fill_char])]


# Тесты.
tests = (
    (([1, 2, 3, 4],), [[1, 2], [3, 4]]),
    (([1, 2, 3, 4, 5],), [[1, 2], [3, 4], [5, None]]),
    (([1, 2, 3, 4, 5, 0], 0), [[1, 2], [3, 4], [5, 0]])
)

for index, item in enumerate(tests):
    res = to_pairs(*item[0])
    assert res == item[1], f'test{index:>02} >>> {item[0]} -> {res} != {item[1]}'


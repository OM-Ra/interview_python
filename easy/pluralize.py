# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать существительные
в единственном числе и возвращать те же существительные,
но если какие-то из них встречаются больше одного раза,
именно эти слова должны возвращаться во множественном числе.

Примеры

pluralize(["cow", "pig", "cow", "cow"])  { "cows", "pig" }
pluralize(["table", "table", "table"])   { "tables" }
pluralize(["chair", "pencil", "arm"])    { "chair", "pencil", "arm" }

Примечания

- Передаваться будут только слова на английском языке.
- Для упрощения будем считать, что множественное число
всегда образуется путем добавления окончания s.
'''

from typing import List

def pluralize(arr: List[str]) -> set:
    '''
    Возвращает множество составленное из
    элементов списка arr. Все повторяющиеся
    слова преобразовываются во множественное
    число добавлением к слову "s".
    '''
    check = ''.join(arr)
    return {item if check.count(item) == 1 else f'{item}s'
            for item in set(arr)}



tests = ((["cow", "pig", "cow", "cow"], { "cows", "pig" }),
         (["table", "table", "table"], { "tables" }),
         (["chair", "pencil", "arm"], { "chair", "pencil", "arm" }))

for arr, check in tests:
    print(pluralize(arr=arr) == check)


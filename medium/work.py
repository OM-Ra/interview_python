# -*- coding: utf-8 -*-

'''
Для транспортирования материалов из цеха А в цех В используется конвейер.
Материалы упаковываются в одинаковые контейнеры и размещаются на ленте
один за одним в порядке изготовления в цехе А.

Каждый контейнер имеет степень срочности обработки в цехе В — float-значение,
где наименьшее означает наивысший приоритет.
То есть, приоритет 1.0 должен выполняться раньше, чем 9.0.

Для упорядочивания контейнеров по степени срочности используют накопитель,
который находится в конце конвейера перед входом в цех В.

Накопитель работает пошагово, на каждом шаге возможны следующие действия:

- накопитель перемещает первый контейнер из ленты в цех В;
- накопитель перемещает первый контейнер из ленты в склад
    (в складе каждый следующий контейнер помещается на предыдущий);
- накопитель перемещает верхний контейнер из склада в цех В.

Напишите программу, которая по последовательности контейнеров определит,
можно ли упорядочить их по степени срочности, пользуясь описанным
накопителем. Предполагается, что на вход всегда приходит список с валидными
значениями или пустой.

Сигнатура: def work(tasks: list) -> bool:
принимает на вход список float и возвращает bool.

Ничего не импортируем, исключения не кидаем!

Примеры:

work([2.9, 2.1]) == True
work([5.6, 9.0, 2.0]) == False
work([ ]) == True
work([1, 1, 1]) == True
'''

from typing import List

def work(tasks: List[float]) -> bool:
    # Отсортированный список - с ним будет сравниваться результат.
    check = sorted(tasks)
    # Стек - склад.
    steck = list()
    # Результат - В цех.
    res = list()
    # Минимальное значение в списке.
    minimum = min(tasks) if tasks else None

    # Проход по значениям списка.
    for item in tasks.copy():

        # Если встречается наименьший текущий элемент списка tasks:
        # item добавляется в список с результатами;
        # item удаляется из списка tasks;
        # ищется новое наименьшее значение в списке.
        if item == minimum:
            res.append(item)
            tasks.remove(item)
            minimum = min(tasks) if tasks else None

        # Если же, стек(склад) не пуст и текущий элемент больше
        # верхнего элемента стека.
        elif steck and item > steck[-1]:

            # Верхние элементы из стека steck добавляются в результирующий
            # список если стек не пуст и текущий элемент item больше
            # верхнего значения стека.
            while steck and item > steck[-1]:
                res.append(steck.pop())

            # Элемент item добавляется в стек если стек пуст либо
            # item меньше или равен верхнему элементу стека.
            # При невыполнении этих условий зразу будет возвращён False.
            if not steck or item <= steck[-1]:
                steck.append(item)
            else:
                return False

        # Во всех остальных случаях элементы добавляются в стек.
        else:
            steck.append(item)

    # Сравнивается полученный результат с сортированным списком.
    return res + steck[::-1] == check


# Тесты.
tests = (
    ([2.9, 2.1], True),
    ([5.6, 9.0, 2.0], False),
    ([], True),
    ([1, 1, 1], True),
    ([1.0, 5.7], True),
    ([5.6, 2.0, 9.0], True),
    ([1, 3.5, 3.5, 2], True),
    ([5, 4, 1, 3, 2], True),
    ([4, 5, 1, 3, 2], False),
    ([10, 9, 8, 11, 12], True)
    )

for tindex, item in enumerate(tests):
    res = work(tasks=item[0])
    assert res == item[1], f'test:{tindex:>02} >>> {item[0]} -> {res} != {item[1]}'

# Ещё тесты.
from itertools import permutations

sum_of_true = sum(work(list(i)) for i in permutations(range(1, 7)))
assert sum_of_true == 132, 'Много True.' \
                           if sum_of_true > 132 \
                           else 'Много False.'


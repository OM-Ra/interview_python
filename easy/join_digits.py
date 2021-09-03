# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать число n и возвращать
строку, состоящую из всех чисел до n включительно. Все цифры
должны отделяться друг от друга дефисами.

Примечание: числа должны идти по порядку, строка должна
начинаться с 1 и заканчиваться последней цифрой числа n.

Примеры:

join_digits(4) "1-2-3-4"
join_digits(11) "1-2-3-4-5-6-7-8-9-1-0-1-1"
join_digits(15) "1-2-3-4-5-6-7-8-9-1-0-1-1-1-2-1-3-1-4-1-5"
'''

def join_digits(nbr: int) -> str:
    # Генирируются необходимые числа и переводятся в строку.
    res = map(str, range(1, nbr + 1))
    # Строки с числами объеденяются в одну строку без разделителей.
    res = ''.join(res)
    # Вставляется разделитель "-" между всеми цифрами.
    return '-'.join(res)


# Тесты.
tests = (
    (4, "1-2-3-4"),
    (11, "1-2-3-4-5-6-7-8-9-1-0-1-1"),
    (15, "1-2-3-4-5-6-7-8-9-1-0-1-1-1-2-1-3-1-4-1-5")
)

for index, item in enumerate(tests):
    res = join_digits(nbr=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


# -*- coding: utf-8 -*-

'''
Задание: Создайте функцию, которая принимает две строки и
вычисляет расстояние Хэмминга между ними.

Расстояние Хэмминга — число позиций, в которых соответствующие
символы двух слов одинаковой длины различны.

Например, в строке «ABCB» на четвертой позиции стоит буква «B»,
а в строке «ABCD» на той же позиции — буква «D».
Расстояние Хэмминга между этими строками — 1.

Примечание: Исходим из того, что передаваемые
строки всегда будут одинаковой длины.

Примеры:

hamming_distance("abcde", "bcdef") 5
hamming_distance("abcde", "abcde") 0
hamming_distance("strong", "strung") 1
hamming_distance("ABBA", "abba") 4
'''

def hamming_distance(line1: str, line2: str) -> int:
    '''
    Вычисление растояния Хэмминга между двумя строками
    одинаковой длины.
    '''
    # Посимвольное сравнение строк и
    # получение суммы по количеству несовпавших символов.
    return sum(item1 != item2
               for item1, item2 in zip(line1, line2))


# Тесты.
tests = (
    (("abcde", "bcdef"), 5),
    (("abcde", "abcde"), 0),
    (("strong", "strung"), 1),
    (("ABBA", "abba"), 4)
)

for index, item in enumerate(tests):
    res = hamming_distance(*item[0])
    assert res == item[1], f'tests:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


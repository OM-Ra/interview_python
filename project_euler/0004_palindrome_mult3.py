# -*- coding: utf-8 -*-

'''
Число-палиндром с обеих сторон (справа налево и слева направо)
читается одинаково. Самое большое число-палиндром, полученное
умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением
двух трехзначных чисел.
'''

def palindrome_mult3(len_mult_nbr: int) -> int:
    # Результат.
    res = 0
    # Получение границ для подбора числа.
    start = int(f'1{"0" * (len_mult_nbr - 1)}')
    stop = int(f'1{"0" * len_mult_nbr}')

    # Перебор первого числа.
    for item1 in range(start, stop):
        # Перебор второго числа.
        for item2 in range(start, stop):
            # Произведение двух числе длинной len_mult_nbr.
            tmp_nbr = item1 * item2
            # Проверка на палиндром и сравнение величины текущего числа.
            if str(tmp_nbr) == str(tmp_nbr)[::-1] and tmp_nbr > res:
                # Сохранение результата.
                res = tmp_nbr

    # Возврат результата.
    return res


# Тесты.
tests = (
    (2, 9009),
    (3, 906609)
)

for index, item in enumerate(tests):
    res = palindrome_mult3(len_mult_nbr=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


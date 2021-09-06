# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать строку —
диапазон букв английского алфавита. Функция должна возвращать
строку из всех букв этого диапазона.

Если в диапазоне заданы заглавные буквы, в результирующей строке
тоже должны быть заглавные.

Примечания:

- диапазон будет задаваться двумя буквами с дефисом между ними
- обрабатывать ошибки не нужно (при указании диапазона обе буквы
будут в одинаковом регистре и располагаться будут в алфавитном порядке).

Примеры:

gimme_the_letters("a-z") "abcdefghijklmnopqrstuvwxyz"
gimme_the_letters("h-o") "hijklmno"
gimme_the_letters("Q-Z") "QRSTUVWXYZ"
gimme_the_letters("J-J") "J"
'''

from string import ascii_letters

def gimme_the_letters(border: str) -> str:
    # Начало среза.
    start = ascii_letters.index(border[0])
    # Конец среза.
    stop = ascii_letters.index(border[2]) + 1

    # Получение среза и возврат результата.
    return ascii_letters[start:stop]


# Тесты.
tests = (
    ("a-z", "abcdefghijklmnopqrstuvwxyz"),
    ("h-o", "hijklmno"),
    ("Q-Z", "QRSTUVWXYZ"),
    ("J-J", "J")
)

for index, item in enumerate(tests):
    res = gimme_the_letters(border=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


# -*- coding: utf-8 -*-

'''
Написать собственную реализацию шифра rot
(подробнее (https://ru.wikipedia.org/wiki/ROT13)).

Функция принимает в себя два параметра: строку,
которую необходимо зашифровать и число, на сколько
позиций смещается символ (по умолчанию - 13).

Пример:

rot("EBG13 rknzcyr.") -> "ROT13 example."
rot("AaBbCcLl.") -> "NnOoPpYy."
rot("Ok, now try rot 6", offset = 6) -> "Uq, tuc zxe xuz 6"
'''

from string import ascii_lowercase, ascii_uppercase

def rot(line: str, offset: int =13) -> str:
    # Изменение строки и возврат результата.
    return line.translate(
        # Шаблон изменения.
        str.maketrans(
            # Символы которые будут изменены.
            f'{ascii_lowercase}{ascii_uppercase}',
            # Символы на которые будет происходить изменение.
            f'{ascii_lowercase[offset:]}{ascii_lowercase[:offset]}' + \
            f'{ascii_uppercase[offset:]}{ascii_uppercase[:offset]}'
        )
    )


# Тесты.
tests = (
    (("EBG13 rknzcyr.",), "ROT13 example."),
    (("AaBbCcLl.",), "NnOoPpYy."),
    (("Ok, now try rot 6", 6), "Uq, tuc zxe xuz 6"),
    (("Uq, tuc zxe xuz 6", -6), "Ok, now try rot 6")
)

for index, item in enumerate(tests):
    res = rot(*item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


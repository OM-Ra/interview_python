# -*- coding: utf-8 -*-

'''
Написать функцию, которая будет переворачивать только буквы.
То есть внутри строки переместиться с начала в конец должны только буквы,
остальные символы (-, =, числа и т.д.) должны остаться на своём месте.

Пример:

reverse_letters("a-bC-dEf-ghIj") -> j-Ih-gfE-dCba
reverse_letters("a-bC=Def+GHi3") -> i-HG=feD+Cba3
reverse_letters("7_28]") -> 7_28]
'''

def reverse_letters(line: str) -> str:
    # Получение итератора из перевёрнутой строки line содержащим только буквы.
    letters = filter(str.isalpha, line[::-1])
    # При встрече буквы в строке line вставляется элемент из итератора letters,
    # иначе - вставляется текущий элемент строки line.
    # Затем результат склеивается в строку и возвращается результат.
    return ''.join(next(letters) if item.isalpha() else item
                   # Проход по символам строки.
                   for item in line)


# Тесты.
tests = (
    ("a-bC-dEf-ghIj", 'j-Ih-gfE-dCba'),
    ("a-bC=Def+GHi3", 'i-HG=feD+Cba3'),
    ("7_28]", '7_28]')
)

for index, item in enumerate(tests):
    res = reverse_letters(line=item[0])
    assert res == item[1], f'tests:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


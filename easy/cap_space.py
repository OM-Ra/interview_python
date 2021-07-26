# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать строку, вставлять
пробелы перед заглавными буквами и переводить всю строку в нижний регистр.

Примеры:

cap_space("helloWorld") -> "hello world"
cap_space("iLoveMyTeapot") -> "i love my teapot"
cap_space("stayIndoors") -> "stay indoors"
'''

def cap_space(s: str) -> str:
    '''
    Вставляет пробелы перед заглавными буквами
    и переводить всю строку в нижний регистр.
    '''
    # Проходит поэлементно по строке и элементы
    # добавляются в новую строку при помощи метода join.
    # Если встречается заглавная буква, тогда такой элемент
    # заменяется на пробел и маленькую букву.
    return ''.join(item if not item.isupper() else f' {item.lower()}'
                   for item in s)



tests = (("helloWorld", "hello world"),
         ("iLoveMyTeapot", "i love my teapot"),
         ("stayIndoors", "stay indoors"))

for s, check in tests:
    print(cap_space(s=s) == check)


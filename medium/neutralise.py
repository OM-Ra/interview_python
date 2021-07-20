# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать две строки,
состоящие из знаков «+» и «-», и возвращать строку —
результат их взаимодействия.

Исходим из того, что строки, передаваемые в функцию,
всегда будут равной длины. Переданные строки
взаимодействуют следующим образом:

- плюс и плюс дают плюс
- минус и минус дают минус
- плюс и минус нейтрализуют друг друга и вместе дают 0.

Разбор примера:

neutralise("+-+", "+--")  "+-0"
# Сравниваем первые символы двух строк, потом следующие два символа и т.д.
# "+" и "+" возвращают "+".
# "-" и "-" возвращают "-".
# "+" и "-" возвращают "0".
# Возвращаем строку символов. 

Другие примеры:

neutralise("--++--", "++--++")  "000000"
neutralise("-+-+-+", "-+-+-+")  "-+-+-+"
neutralise("-++-", "-+-+")      "-+00"
'''

def neutralise(s1: str, s2: str) -> str:
    '''
    Возвращает результирующую строку после
    кодировки по двум строкам. Новый символ
    определяется по соответствующим символам
    в двух строках:
    1) + и + дают +;
    2) - и - дают -;
    3) + и - или - и + дают 0.
    '''
    # Список с шифрами
    code = ['0', '+', '-']
    # Определяется наличие символов и по результату
    # получаем индекс шифра который дают оба символа (x + y)
    func = lambda x, y: code[('+' in x + y) - ('-' in x + y)]
    # Применяем функцию к каждому символу попарно для обеих
    # строк и склеиваем результат в строку.
    return ''.join(map(func, s1, s2))



tests = ((("+-+", "+--"), "+-0"),
         (("--++--", "++--++"), "000000"),
         (("-+-+-+", "-+-+-+"), "-+-+-+"),
         (("-++-", "-+-+"), "-+00"))

for args, check in tests:
    print(neutralise(*args) == check)


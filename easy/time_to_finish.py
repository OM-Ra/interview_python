# -*- coding: utf-8 -*-

'''
Представьте, что вы на экзамене.
Время вышло, преподаватель говорит дописать
предложение до точки и сдать работу.

Допустим, написание одной буквы занимает
0,5 с (пробелы не учитываем).

Напишите функцию, которая будет принимать
полное и недописанное предложение, а возвращать
время, необходимое на дописывание (в секундах).

Пример:

time_to_finish("And so brings my conclusion to its conclusion.",
    "And so brings my conclusion to")    7
'''

SEC = 0.5

def time_to_finish(full_s: str, short_s: str) -> float:
    '''
    Вычисляет время за которое будет дописана строка
    short_s до строки full_s. Один непробельный
    символ занимает время набора 0.5 (с).
    '''
    # Получение остатка строки без пробельных символов
    full_tmp_s = full_s[len(short_s):].replace(' ', '')
    # Вычисление результата
    return len(full_tmp_s) * SEC



full_s = "And so brings my conclusion to its conclusion."
short_s = "And so brings my conclusion to"
check = 7
print(time_to_finish(full_s=full_s, short_s=short_s) == check)


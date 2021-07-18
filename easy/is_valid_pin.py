# -*- coding: utf-8 -*-

'''
Задание:
Напишите функцию для проверки, является ли строка валидным PIN-кодом.

Валидный PIN-код:
- состоит ровно из 4 или 6 символов
- состоит только из цифр (0-9)
- не содержит пробелов.

Примечание: на вход всегда приходит строка (не нужно это проверять), при вводе пустых строк результат должен быть False. Функция не должна бросать исключений

Примеры:

is_valid("1234") ➞ True
is_valid("45135") ➞ False
is_valid("89abc1") ➞ False
is_valid("900876") ➞ True
is_valid(" 4983") ➞ False
'''

def is_valid_pin(pin: str) -> bool:
    '''Проверяет валидность pin-кода.'''
    return pin.isdigit() and len(pin) in (4, 6)

pins = (('1234', True), ('45135', False), ('89abc1', False),
        ('900876', True), (' 4983', False))

for pin, check in pins:
    print(is_valid_pin(pin=pin) == check)


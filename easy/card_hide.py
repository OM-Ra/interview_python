# -*- codig: utf-8 -*-

'''
Задание:
Напишите функцию, которая будет принимать номер
кредитной карты и показывать только последние 4 цифры.
Остальные цифры должны заменяться звездочками.

Примечания:
- вернуть нужно строку
- длина строки должна быть такой же, как у введенной.

Примеры:

card_hide("1234123456785678") ➞ "************5678"
card_hide("8754456321113213") ➞ "************3213"
card_hide("35123413355523") ➞   "**********5523"
'''

def card_hide(nbr_card: str) -> str:
    '''Возвращает номер карты спрятаный * кроме последних 4 цифр.'''
    return f'{"*" * (len(nbr_card) - 4)}{nbr_card[-4:]}'



cards = (("1234123456785678", "************5678"),
         ("8754456321113213", "************3213"),
         ("35123413355523", "**********5523"))

for card, check in cards:
    print(card_hide(nbr_card=card) == check)


# -*- coding: utf-8 -*-

'''
Завод по производству фруктовых соков помечает свою продукцию
специальными идентификаторами. Каждый ID составляется из трех
первых букв названия фрукта и объема упаковки.

Напишите функцию, которая будет создавать ID продукта для фруктовых соков.

Примеры:
 get_drink_ID("apple", "500ml") "APP500"
 get_drink_ID("pineapple", "45ml") "PIN45"
 get_drink_ID("passion fruit", "750ml") "PASFRU750"

Примечания:
- Объем упаковки будет передаваться в виде строки, всегда в миллилитрах.
- Буквы нужно возвращать в верхнем регистре.
'''

def get_drink_ID(name: str, volume: str) -> str:
    '''Создаёт идинтификатор из имени и объёма.'''
    # Первая часть id из name: берутся 3 первые буквы каждого слова.
    id1 = ''.join(item[:3]for item in name.upper().split())
    # Вторая часть id из volume: берётся только число.
    id2 = ''.join(item for item in volume if item.isdigit())
    # Результат форматируется в одну строку.
    return f'{id1}{id2}'



tests = ((("apple", "500ml"), "APP500"),
         (("pineapple", "45ml"), "PIN45"),
         (("passion fruit", "750ml"), "PASFRU750"))

for args, check in tests:
    print(get_drink_ID(*args) == check)


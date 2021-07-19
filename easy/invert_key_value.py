# -*- codong: utf-8 -*-

'''
Напишите функцию, которая будет менять местами
ключи и значения в словаре.

Примеры:

invert({ "z": "q", "w": "f" })
{ "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
{ 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
{ "koala": "zebra", "camel": "horse" }
'''

def invert_key_value(data: dict) -> dict:
    '''Меняет в словаре местами ключи и значения.'''
    return {value:key for key, value in data.items()}



datas = (({ "z": "q", "w": "f" }, { "q": "z", "f": "w" }),
         ({ "a": 1, "b": 2, "c": 3 }, { 1: "a", 2: "b", 3: "c" }),
         ({ "zebra": "koala", "horse": "camel" }, { "koala": "zebra", "camel": "horse" }))

for data, check in datas:
    print(invert_key_value(data=data) == check)


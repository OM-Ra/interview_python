# -*- coding: utf-8 -*-

'''
При импорте объектов из модуля в Python
обычно используется следующий синтаксис:

from module_name import object
 
Напишите функцию, которая будет принимать
неверно составленную инструкцию импорта и
возвращать правильную. Передаваться в функцию
будут исключительно неправильно составленные
инструкции.

Примеры
fix_import("import object from module_name")  "from module_name import object"
fix_import("import randint from random")  "from random import randint"
fix_import("import pi from math")  "from math import pi"
'''

def fix_import(s: str) -> str:
    '''
    Из строки неправильного формата импората
    делает правильный и возвращает правильную строку.
    '''
    s = s.split()
    return f'from {s[-1]} import {s[1]}'



tests = (("import object from module_name", "from module_name import object"),
         ("import randint from random", "from random import randint"),
         ("import pi from math", "from math import pi"))

for s, check in tests:
    print(fix_import(s=s) == check)


# -*- coding: utf-8 -*-

''' 
Ваша задача — написать функцию, которая будет переводить
CamelCase и Lower CamelCase в Lowercase с подчеркиванием.

Пример:

change_to_lower("SomeClassName") -> some_class_name
change_to_lower("variableName") -> variable_name
change_to_lower("test") -> test
'''

def change_to_lower(s: str) -> str:
    '''
    
    '''
    # Проход по всем символам верхнего регистра
    for item in [sym for sym in set(s) if sym.isupper()]:
        # Строка переписывается так, чтобы в ней появились пробелы
        # до символов верхнего регистра и эти же символы
        # заменяются на нижний регистр
        s = s.replace(item, f' {item.lower()}')
    # Строка разбивается по пробелам и склеивается символом "_"
    return '_'.join(s.split())



tests = (("SomeClassName", 'some_class_name'),
         ("variableName", 'variable_name'),
         ("test", 'test'))

for s, check in tests:
    print(change_to_lower(s=s) == check)


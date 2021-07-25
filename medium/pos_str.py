# -*- coding: utf-8 -*-

'''
Ваша задача — написать метод, который будет позиционировать строку. 
Он принимает саму строку, а после align со значениями left, center 
или right (по умолчанию - left) и длину возвращаемой строки.
'''

def pos_str(string: str, align: str ='left', max_len: int =20) -> str:
    '''Форматирует строку string длиной max_len по параметру align.'''
    # Словарь с форматируемыми операторами
    oper = {'left': '<', 'right': '>', 'center': '^'}
    # Форматирование строки
    return f'{string:{oper.get(align, "<")}{max_len}}'



tests = (({'string': 'hello world', 'align': 'left'}, 'hello world         '),
         ({'string': 'hello world', 'align': 'right'}, '         hello world'),
         ({'string': 'hello world', 'align': 'center'}, '    hello world     '),
         ({'string': 'hello world', 'align': 'center', 'max_len': 30}, '         hello world          '),
         ({'string': 'hello world', 'align': 'right', 'max_len': 30}, '                   hello world'))

for kwargs, check in tests:
    print(pos_str(**kwargs) == check)


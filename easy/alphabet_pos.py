# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая будет возвращать
список из позиций букв в алфавите. 

alphabet_pos("Lorem ipsum dolor sit amet")
[12, 15, 18, 5, 13, 9, 16, 19, 21, 13, 4, 15, 12, 15, 18, 19, 9, 20, 1, 13, 5, 20]

alphabet_pos("Oh no, its \n\t123t.!?")
[15, 8, 14, 15, 9, 20, 19, 20]
'''

from typing import List
from string import ascii_lowercase as lower_case

def alphabet_pos(txt: str) -> List[int]:
    '''Возвращает список с позициями букв в английском алфавите.'''
    return [lower_case.index(item) + 1
            for item in txt.lower()
            if item.isalpha()]



tests = (("Lorem ipsum dolor sit amet", [12, 15, 18, 5, 13, 9, 16, 19, 21, 13, 4, 15, 12, 15, 18, 19, 9, 20, 1, 13, 5, 20]),
         ("Oh no, its \n\t123t.!?", [15, 8, 14, 15, 9, 20, 19, 20]))

for txt, check in tests:
    print(alphabet_pos(txt=txt) == check)


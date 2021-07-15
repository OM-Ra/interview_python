# -*- coding: utf-8 -*-

"""
Ваша цель — написать функцию,
которая находит самые повторяющиеся слова в строке.

Пример:

text ('Am I want write code? Yeah! I like it') → I
text ('Hi! How are you? Hi! I am ok') → Hi
text ('test text test and test that again') → test
"""

from collections import Counter

def text(string: str) -> str:
    '''Возвращает наиболее часто встречаемое слово.'''
    words = Counter(string.split())
    return words.most_common(1)[0][0]



lines = (('Am I want write code? Yeah! I like it', 'I'),
         ('Hi! How are you? Hi! I am ok', 'Hi!'),
         ('test text test and test that again', 'test'))

for string, check in lines:
    print(text(string=string) == check)


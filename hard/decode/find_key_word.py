# -*- coding: utf-8 -*-

from math import floor
from collections import Counter

def find_min_value(counts: Counter) -> int:
    '''Находит минимальное число вхождений во фразе ключе.'''
    return counts.most_common()[-1][1]

def find_min_len_key_word(counts: Counter) -> int:
    '''Находит минимальную длину фразы ключа.'''
    # минимальное число вхождений символа
    min_count = find_min_value(counts=counts)
    # сумма всех вхождений
    sum_values = sum(counts.values())
    return floor(sum_values / min_count)

def check_key_phrase(key_phrase: str, len_key_word: int) -> bool:
    '''Возвращает истину если искомая фраза найдена.'''
    # Сделаем предположение, что если фраза подобрана правильно,
    # тогда заменив эту фразу в повторяющейся фразе на "" -
    # мы получим либо пустую строку, либо остаток строки который
    # будет полностью входить в найденную фразу, что будет означать -
    # правильность фразы.
    s = key_phrase.replace(key_phrase[:len_key_word], '')
    if s:
        return True if key_phrase[:len_key_word].find(s) > -1 else False
    return True

def find_key_word(key_phrase: str) -> str:
    '''
    Нахожит искомую фразу-ключ без повторений.

    key_phrase - повторяющаяся фраза-ключ.
    '''
    # Сделаем предположение, что минимальная длина искомой фразы
    # будет такая как, вхождение символа в повторяющуюся фразу ключ
    # разделённое на минимальное вхождение символа в эту фразу
    # даст количество символов входящих в эту фразу.

    # Словарь с количеством вхождений уникальных символов
    counts = Counter(key_phrase)
    len_key_word = find_min_len_key_word(counts=counts)
    # Начинаем подбор длины фразы, от минимального до всей длины
    # повторяющейся фразы.
    for nbr in range(len_key_word, len(key_phrase) + 1):
        if check_key_phrase(key_phrase=key_phrase, len_key_word=nbr):
            return key_phrase[:nbr]


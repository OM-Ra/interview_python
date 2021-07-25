# -*- coding: utf-8 -*-

'''
Ваша задача — написать метод, который будет обрезать строку до
определённой длины и добавлять в конец троеточие.
Если текст короче или же равен max_len, то ничего не меняем.

Пример:
cut_str("Hello world!") -> Hello worl...
text = "Lorem Ipsum is simply dummy text"
cut_str(text) -> Lorem Ipsu...
cut_str(text, max_len=12) -> Lorem Ipsum...
cut_str(text, max_len=40) -> Lorem Ipsum is simply dummy text
'''

def cut_str(s: str, max_len: int =10) -> str:
    '''Обрезает строку s до длины max_len и добавлет многоточие.'''
    # Строка форматируется следующим образом:
    # - делается срез от начала строки до max_len;
    # - обрезаются пробельные символы справа;
    # - если длина строки больше max_len - тогда добавляется многоточие.
    return f'{s[:max_len].rstrip()}{"..." * (len(s) > max_len)}'



tests = (({"s": "Hello world!"}, "Hello worl..."),
         ({"s": "Lorem Ipsum is simply dummy text"}, "Lorem Ipsu..."),
         ({"s": "Lorem Ipsum is simply dummy text", "max_len": 12}, "Lorem Ipsum..."),
         ({"s": "Lorem Ipsum is simply dummy text", "max_len": 40}, "Lorem Ipsum is simply dummy text"))

for kwargs, check in tests:
    print(cut_str(**kwargs) == check)


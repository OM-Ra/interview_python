# -*- coding: utf-8 -*-

'''
Олегу не хочется становиться старше, поэтому он решил праздновать
только свое 20-летие (ну и 21 год тоже, ладно уж). Это возможно,
если применить некоторые математические навыки. Нужно просто
подобрать подходящее основание числа!

Например, если сейчас Олегу 22 года, это 20 с основанием 11.
Аналогично 65 лет — это ровно 21 год с основанием 32.
И так далее.

Создайте функцию, которая будет принимать текущий возраст age
и возвращать «нужный» возраст (20 лет или 21 год), а также
основание числа в том же формате, что в примерах.

Примеры:
happy_birthday(22) "Oleg is just 20, in base 11!"
happy_birthday(65) "Oleg is just 21, in base 32!"
happy_birthday(83) "Oleg is just 21, in base 41!"

Примечание: передваемый в функцию возраст всегда будет больше 21.
'''
# Итератор без ограничения.
from itertools import count

def happy_birthday(age: int) -> str:
    '''
    Вычисляет основание для числа 20 или 21 так, чтобы получилось
    число age. И возвращает строку в форматированном виде с
    результатом.
    '''
    # Начиная с основания 11 будет подбирать необходимое основание.
    for base in count(11):
        # Перебор по искомому числу под основание base.
        for nbr in (20, 21):
            # Проверяет соответствие числа и основания с искомым age.
            if sum(digit * base ** index
                   for index, digit in enumerate(map(int, str(nbr)[::-1]))) == age:
                # Когда число и основание подобраны правильно результат
                # форматируется в нужную строку.
                return f'Oleg is just {nbr}, in base {base}!'



tests  = ((22, "Oleg is just 20, in base 11!"),
          (65, "Oleg is just 21, in base 32!"),
          (83, "Oleg is just 21, in base 41!"))

for age, check in tests:
    print(happy_birthday(age=age) == check)


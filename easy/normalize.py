# -*- coding: utf-8 -*-

'''
Задание: 

22 октября — ДЕНЬ CAPS LOCK. За исключением этого дня, все предложения
должны быть в нижнем регистре. Поэтому напишите функцию для
нормализации предложения.

Эта функция должна принимать строку. Если строка состоит только из
символов верхнего регистра, переведите их в нижний регистр и добавьте
в конце восклицательный знак.

Примечания:
- каждая передаваемая в функцию строка - отдельное предложение
- предложение после нормализации должно начинаться с заглавной буквы
- восклицательный знак добавляем к предложениям,
которые переводили из верхнего регистра в нижний.

Примеры:

normalize("CAPS LOCK DAY IS OVER") "Caps lock day is over!"
normalize("Today is not caps lock day.") "Today is not caps lock day."
normalize("Let us stay calm, no need to panic.") "Let us stay calm, no need to panic."
'''

def normalize(line: str) -> str:
    '''
    Проверяет состоит ли строка line только из символов
    верхнего регистра.
    
    Return:
        - Переводит символы в нижний регист кроме первого
          и добавляет восклицательный знак в конец строки.
        - Возвращает строку line без изменений если строка
          состоит не только из символов верхнего регистра.
    '''
    # Проверка всех регистрозависимых символов на верхний регистр.
    if line.isupper():
        # Преобразование строки и возврат результата.
        return f'{line.capitalize()}!'
    # Возврат строки line без изменений.
    return line


# Тесты.
tests = (
    ("CAPS LOCK DAY IS OVER", "Caps lock day is over!"),
    ("Today is not caps lock day.", "Today is not caps lock day."),
    ("Let us stay calm, no need to panic.", "Let us stay calm, no need to panic.")
)

for index, item in enumerate(tests):
    res = normalize(line=item[0])
    assert res == item[1], f'tests:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


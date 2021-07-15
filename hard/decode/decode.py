# -*- coding: utf-8 -*-

from base64 import b64decode
# символы которые, по условию, могут быть ключём
from string import ascii_letters
# функция нахождения фразы-ключа
from find_key_word import find_key_word

# изначальный текст который был зашифрован
txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."

def decode(s: str) -> str:
    '''
    Находит фразу ключ, но равной длине всего текста,
    т.е. она будет повторяться.
    '''
    key_phrase = '' # искомый ключ для шифрования
    s = b64decode(s).decode('UTF-8') # перевод текста из бинарного формата

    for i, char_code_txt in enumerate(s): # зашифрованыый текст
        for char_key in ascii_letters:    # подбор искомого символа ключа
            # шифрование исходного символа по известному алгоритму
            check_char = chr(ord(txt[i]) + ord(char_key))
            # сравнение нового символа с уже зашифрованным символом
            if char_code_txt == check_char:
                # получится повторяющийся ключ
                key_phrase += char_key

    return key_phrase



# файл с текстом который был получен после шифрования
name_file = 'result.txt'

with open(name_file, 'r') as fd:
    txt_code = fd.read()

key_phrase = decode(s=txt_code)  # зацикленная фраза ключ

print(find_key_word(key_phrase=key_phrase))


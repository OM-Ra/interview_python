'''
У вас есть алгоритм, начальный текст и результат его работы.
Ваша задача — узнать ключ шифрования - key.

Ключ состоит только из ASCII символов и только из больших и маленьких
букв английского алфавита.

• Исходный код — файл test2.py
• Результат — файл result.txt
'''

import sys
from base64 import b64encode

# key = sys.argv[1] # TODO: Добавить проверку входных значений и вывода usage
# TODO: Сделать возможность считывать с файла
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in \
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."

key = 'HelloWorld' # Это необходимо найти.

def encode(string):
    result = ""
    for i, data in enumerate(string):
        index = i % len(key)
        num_of_char = ord(data) + ord(key[index])
        result += chr(num_of_char)
    return b64encode(bytes(result, 'utf-8'))

with open('result.txt', 'wb') as file:
    file.write(encode(text))


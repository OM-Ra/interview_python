# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать строку и
возвращать отсортированный список трехбуквенных групп. 

Список формируется следующим образом: берем первые
три буквы строки, затем сдвигаемся на одну букву и
берем следующие три буквы и т. д. Если в переданной
строке меньше трех букв, нужно вернуть пустой список.

Разбор примера
three_letter_collection("python")  ["hon", "pyt", "tho", "yth"]
# 1-я группа: "hon"
# 2-я группа: "pyt"
# 3-я группа: "tho"
# 4-я группа: "yth"
# Не забудьте отсортировать список! 

Другие примеры
three_letter_collection("slap")  ["lap", "sla"]
three_letter_collection("click") ["cli", "ick", "lic"]
three_letter_collection("cat")   ["cat"]
three_letter_collection("hi")    []
'''

from typing import List

def three_letter_collection(s: str) -> List[str]:
    '''
    Формируется список содержащий группу строк
    состоящих из трёх символов образованных из
    строки s.
    Строки формируются так: берем первые три буквы
    строки, затем сдвигаемся на одну букву и
    берем следующие три буквы и т. д.
    '''
    res = [s[index:index + 3]
           for index in range(len(s) - 2)]
    return sorted(res)



tests = (("slap", ["lap", "sla"]),
         ("python", ["hon", "pyt", "tho", "yth"]),
         ("click", ["cli", "ick", "lic"]),
         ("cat", ["cat"]),
         ("hi", []))

for s, check in tests:
    print(three_letter_collection(s=s) == check)


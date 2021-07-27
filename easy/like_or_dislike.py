# -*- coding: utf-8 -*-

'''
На YouTube есть функционал лайков и дизлайков.
Выбирая между двумя кнопками, вы можете выразить свое мнение о контенте.
При этом настройки не позволяют одновременно и лайкнуть,
и дизлайкнуть видео.

Есть и другие правила для этой функции:

1. Если нажать какую-либо из кнопок повторно, это отменит первое
нажатие (т.е. лайк или дизлайк просто снимется).
2. Если вы нажали кнопку лайка после того как уже нажали
дизлайк, значение перезаписывается (вместо дизлайка будет стоять лайк).
И наоборот.

Напишите функцию, которая будет принимать список нажатий кнопок и
возвращать итоговое состояние.

Примеры:
like_or_dislike(["Dislike"]) "Dislike"
like_or_dislike(["Like", "Like"]) "Nothing"
like_or_dislike(["Dislike", "Like"]) "Like"
like_or_dislike(["Like", "Dislike", "Dislike"]) "Nothing"

Примечания:
Если никакая из кнопок не активна, возвращаем «Nothing».
Если список пуст, тоже возвращаем «Nothing».
'''

from typing import List

def like_or_dislike(arr: List[str]) -> str:
    '''
    '''
    # Результаты нажатий кнопок.
    res = 'Nothing'
    # Если элемент не равен предыдущему элементу, тогда
    # res присваивается текущий элемент, иначе
    # присваивается Nothing.
    [res := item if item != res else 'Nothing'
     for item in arr]
    # Возвращается итоговое полученное значение.
    return res



tests = ((["Dislike"], "Dislike"),
         (["Like", "Like"], "Nothing"),
         (["Dislike", "Like"], "Like"),
         (["Like", "Dislike", "Dislike"], "Nothing"),
         ([], "Nothing"))

for arr, check in tests:
    print(like_or_dislike(arr=arr) == check)


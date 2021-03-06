# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет возвращать True, если строка,
являющаяся аргументом функции, содержит возрастающие И
последовательные числа. Например, ‘123’ (1-2-3) или ‘101112’ (10-11-12).

Сигнатура — def ascending(value: str) -> bool:

Примечания:

- Функция должна возвращать (не печатать!) только True\False,
    она не должна бросать исключений.
- Предполагается, что строка-аргумент никогда не пустая и всегда содержит
    минимум 2 числа, например ’10’ — валидная строка.
- Строка-аргумент будет содержать только числа.

Примеры:

ascending("232425") -> True
# строку можно представить как
# 23, 24, 25, а эти числа следуют друг за другом по возрастанию

ascending("2324256") -> False
# шестерка в конце ломает возрастающий ряд

ascending("444445") -> True
# строку можно представить как 444 и 445
'''

def ascending(value: str) -> bool:
    '''
    Проверяет содержит ли строка value возрастающие и
    последовательные числа.
    '''
    # Подбор шага. Максимальный шаг не может быть больше
    # половины длины строки value.
    for step in range(1, len(value) // 2 + 1):
        # По варианту шага step проверяется разность двух чисел
        # которая должна равняться еденице.
        if all(( int(value[index + step: index + step * 2]) -
                 int(value[index: index + step])
                 == 1 )
               # Проход по индексам строки для поиска чисел.
               for index in range(0, len(value) - step, step)):
            # Если все числа в строке соответствуют заданным условиям.
            return True
    # Если все варианты шага step не дали результат, значит
    # строка неудовлетворяет условию.
    return False



tests = (("232425", True), ("2324256", False), ("444445", True))

for value, check in tests:
    print(ascending(value=value) == check)


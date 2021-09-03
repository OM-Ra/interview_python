# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая проверяет синтаксис калькулятора.
То есть обычные действия +. -, /, * и скобки.

eval - использовать запрещено.

Пример:

check_syntax("( 1 + 2 )") -> True
check_syntax("( 1 + )") -> False
check_syntax("1 + -22") -> True
check_syntax("(1 + -22") -> False
'''

import re

def delete_brackets(line: str) -> str:
    '''Удаляет скобки и пробелы.'''
    return line.translate(str.maketrans('()', '  ')).replace(' ', '')

def check_brackets(line: str) -> bool:
    '''Проверяет правильность скобок.'''
    # Стек.
    steck = list()
    # Получение строки только из скобок.
    line_breckets = ''.join(re.findall('[()]', line))

    # Проход по элементом полученной строки.
    for item in line_breckets:
        # Если скобка открывающаяся, тогда она кладётся в стек.
        if item == '(':
            steck.append(item)
        # Если скобка закрывающаяся и стек пуст или в нём не открывающаяся скобка
        # тогда из функции возвращается False. 
        elif item == ')' and (not steck or steck.pop() != '('):
            return False

    # Если стек пуст и строка без скобок не пустая тогда вернётся True.
    return True \
           if not steck and delete_brackets(line) \
           else False

def find_index_next_digit(arr: list, pos: int) -> int:
    '''Находит индекс числа стоящего дальше индекса pos.'''
    while not arr[pos].isdigit():
        pos += 1
    return pos

def check_sym(arr: list) -> bool:
    '''Проверяет правильность операторов.'''
    # Индек (позиция) элемента в списке.
    pos = 0
    # Допустимые операторы.
    sym1 = '*/'
    sym2 = '+-'

    # Перебераем позицию элемента в списке.
    while pos < len(arr):

        # Если символ является одним из символов sym2.
        if arr[pos] in sym2:

            # Проход по всем элементам до следующего числа или
            # символа из группы sym1.
            while arr[pos] not in sym1 and not arr[pos].isdigit():
                pos += 1

            # Если встретился символ из группы sym1 тогда возвращается False.
            if arr[pos] in sym1:
                return False

        # Если встретился символ из группы sym1.
        elif arr[pos] in sym1:
            # Сохранение текущей позиции элемента списка.
            tmp_pos = pos
            # Нахождение позиции числа идущего после текущей позиции tmp_pos.
            pos = find_index_next_digit(arr, pos)

            # Если операторов из группы sym1 больше двух тогда
            # из функции вернётся False.
            if sum(item in sym1 for item in arr[tmp_pos:pos]) > 2:
                return False

            # В случае, если операторов группы sym1 меньше или равно 2
            # тогда проверка будет продолжена.

            # Сохранение текущего оператора.
            tmp_sym = arr[tmp_pos]
            # Проход по позициям до следующего числа.
            while tmp_pos < pos:

                # Если текущий оператор не развен сохранённому
                # и любой из операторов до следующего числа
                # входит в группу sym1 - из функции вернётся False.
                if arr[tmp_pos] != tmp_sym and \
                   any(arr[index] in sym1
                       for index in range(tmp_pos, pos)):
                    return False

                # Увеличение позиции элемента для текущей проверки.
                tmp_pos += 1

        # Увеличение позиции элемента для всего списка.
        pos += 1

    return True
            

def check_line(line: str) -> bool:
    '''Проверяет правильность строки не учитывая скобок.'''
    # Группы допустимых операторов.
    sym1 = '*/'
    sym2 = '+-'

    # Удаление скобок.
    line = delete_brackets(line)
    # Удаление пустых строк из списка разбитого по операторам (включая операторы).
    line = [item
            for item in re.split('([*/+\-])', line)
            if item]
    
    # Проверка отсутствия недопустимых символов.
    if not all(item in sym1 + sym2 or item.isdigit()
               for item in line):
        return False
    # Проверка первого и последнего символа, чтобы
    # они были допустимыми.
    if line and line[-1] in sym1 + sym2 or line[0] in sym1:
        return False

    # Возврат результата после проверки операторов.
    return check_sym(arr=line)
    

def check_syntax(line: str) -> bool:
    # Проверяются наличие строки, правильность скобок
    # и остальноого синтаксиса.
    if line and (not check_brackets(line) or not check_line(line)):
        return False
    return True


# Тесты.
tests = (
    ('', True),    # С нулевым тестом можно поспорить, так что его можно убрать или изменить вывод.
    ('((()))', False),
    ('(()))', False),
    ('((()))(', False),
    ('()(())((()))', False),
    ('(((1 + 1)))', True),
    ('(((1)))', True),
    ('9', True),
    ("(1 + -22", False),
    ("( 1 + 2 )", True),
    ("( 1 + )", False),
    ("1 + -22", True),
    ("1+--+22", True),
    ("-5 + 8", True),
    ("1 + -22)", False),
    ('-3 + 1 -', False),
    ('3 + * 5', False),
    ('3 * + 5', True),
    ('3 + * - / 9', False),
    ('3 - / 5', False),
    ('3 / - 5', True),
    ('+ 1', True),
    ('* 9', False),
    ('5 ** 2', True),
    ('5 *** 2', False),
    ('5 ***+ 2', False),
    ('5 * +++---+++ 3', True),
    ('5 * +++---+++ * 3', False),
    ('5 */ 2', False),
    ('(5 + a)', False),
    ('(5 + 4) + (9 ** 2)', True),
    ('(5 + 4) + {9 ** 2}', False),
    ('10 // 3', True)
)

for index, item in enumerate(tests):
    res = check_syntax(line=item[0])
    assert res == item[1], f'test:{index:>02} >>> {item[0]} -> {res} != {item[1]}'


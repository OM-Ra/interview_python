# -*- coding: utf-8 -*-

'''
Ваша задача — написать функцию, которая уберёт повторяющиеся
элементы из списка, но оставит их в том же порядке. 

unique_order("AAABBBCCCDAAABBB") ["A", "B", "C", "D", "A", "B"]
unique_order("ABBCcAD") ["A", "B", "C", "c", "A", "D"]
unique_order([1, 2, 2, 3, 3]) [1, 2, 3]

P.S. использовать сторонние модули нельзя
'''

def unique_order(data) -> list:
    '''
    Возвращает список полученный из data с элементами в
    том же порядке, что и в data, но без повторений.
    '''
    # Результирующий список.
    res = [data[0]] if data else list()
    # Проход по всем элементам data и добавление каждого элемента
    # в список res но без повторений.
    [res.append(item) for item in data if item != res[-1]]
    return res



tests = (("AAABBBCCCDAAABBB", ["A", "B", "C", "D", "A", "B"]),
         ("ABBCcAD", ["A", "B", "C", "c", "A", "D"]),
         ([1, 2, 2, 3, 3], [1, 2, 3]))

for data, check in tests:
    print(unique_order(data=data) == check)


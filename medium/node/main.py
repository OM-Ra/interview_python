# -*- coding: utf-8 -*-

'''
Напишите функцию которая принимает два
аргумента: бинарное дерево и значение
в виде числа. А возвращает ближайшее
значение найденное в бинарном дереве.
'''

from node import Node

def check_left(node: object, value: int, res: int) -> bool:
    '''
    Проверяет валидность захода влево.
    node - узел бинарного дерева.
    value - искомое значение.
    res - ближайшее значение узла к value, на данный момент.
    '''
    if node.left and abs(node.left.data - value) < res:
        if node.right:
            return abs(node.left.data - value) < abs(node.right.data - value)
        return True
    return False

def go_tree_nodes(node: object, value: int, res: int) -> int:
    '''
    Обход бинарного дерева node и поиск ближайшего значения узла
    к value.
    res - ближайшее значение узла к value, на данный момент.
    '''
    if node:
        if node.data == value:
            return node.data
        elif check_left(node, value, res):
            return go_tree_nodes(node.left, value, node.left.data)
        elif node.right and abs(node.right.data - value) < res:
            return go_tree_nodes(node.right, value, node.right.data)
        else:
            return res

def find_value_in_node(node: object, value: int) -> int:
    '''
    Возвращает значение узла бинарного дерева node
    которое равно или наиболее близко к value.
    '''
    return go_tree_nodes(node, value, node.data)



node00 = Node(data=9)
node01 = Node(data=8)
node02 = Node(data=10)
node03 = Node(data=7)
node04 = Node(data=11)

node00.left = node01
node01.left = node03
node00.right = node02
node02.right = node04

tests = ((4, 7), (9, 9), (11, 11), (15, 11), (10, 10))

for value, check in tests:
    print(find_value_in_node(node00, value) == check)


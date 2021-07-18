# -*- coding: utf-8 -*-

from typing import Any

class Node:
    '''Класс узла бинарного дерева.'''

    def __init__(self, data: Any) -> None:
        self.left = None
        self.right = None
        self.data = data


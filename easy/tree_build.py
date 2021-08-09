# -*- coding: utf-8 -*-

'''
Необходимо написать код, который будет создавать пирамиду,
принимая её кол-во уровней.

pyramid(5)
    *    
   ***   
  *****  
 ******* 
*********

Можете усложнить себе задачу и сделать ёлочку как на изображении ниже.

tree_build(10) ->
         *         
        ***        
       *****       
        ***        
     *********     
    ***********    
     *********     
  ***************  
 ***************** 
  ***************  

Удаление будет происходить только, если уровень делится нацело на 3.
'''

from typing import List

def construct_str(arr: List[str], height: int) -> str:
    '''
    Элементы списка arr склеиваются в одну строку
    и каждая строка списка центрируется по максимальной длине строки
    зависящей от height.
    '''
    # Функция для центрирования строки по максимальной длине
    # строки всей пирамиды
    func = lambda string: string.center(height * 2 - 1)
    # Склеивание в одну строку элементов списка после
    # применения к ним функции func
    return '\n'.join(map(func, arr))

def pyramid(height: int) -> str:
    '''Возвращает строку классической пирамиды высотой height.'''
    # Максимальная длина строки
    len_str = height * 2 - 1
    # Список для строк пирамиды
    res = ['*'] if height > 0 else ['']
    for _ in range(height - 1):
        # Каждая новая строка длинее предыдущей на два символа
        res.append(f'{res[-1]}**')
    return construct_str(arr=res, height=height)

def tree_build(height: int) -> str:
    # Максимальная длина строки
    len_str = height * 2 - 1
    # Получение классической пирамиды
    res = pyramid(height).split('\n')
    # Проходим по каждому третьему элементу начиная с 3
    for index in range(3, height, 3):
        # Создание новой строки и её центрирование
        # по максимальной длине строки
        res[index] = f"{'*' * (res[index].count('*') - 4):^{len_str}}"
    # Склеивание списка в одну строку и возврат результата
    return '\n'.join(res)
    
        

tests = ((10, '''         *         
        ***        
       *****       
        ***        
     *********     
    ***********    
     *********     
  ***************  
 ***************** 
  ***************  '''),)

for height, check in tests:
    print(tree_build(10) == check)

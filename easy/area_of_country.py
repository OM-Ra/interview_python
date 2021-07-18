# -*- coding: utf-8 -*-

"""
Задание:
Напишите функцию, которая будет принимать в качестве
аргументов  название страны (name) и ее площадь (area)
и возвращать процентное отношение площади страны к
площади земной суши.

Примечания:
- площадь земной суши составляет  148940000 кв. км
- результат нужно округлить до сотых.
- строка будет не пустой, площадь всегда будет
  целым положительным числом (не нужно это проверять!)

Примеры:

area_of_country('Russia', 17098242) ➞ 'Russia is 11.48% of the total world's landmass'
area_of_country('USA', 9372610) ➞     'USA is 6.29% of the total world's landmass'
area_of_country('Iran', 1648195) ➞    'Iran is 1.11% of the total world's landmass'
"""

# Площадь земной суши
WORLD_AREA = 148940000

def area_of_country(name: str, area: int) -> str:
    '''
    Возвращает строку с процентным отношением площади area
    для страны name по отношению к всей площади суши.
    '''
    res = round(area / WORLD_AREA * 100, 2)
    return f"{name} is {res}% of the total world's landmass"



areas = (('Russia', 17098242, "Russia is 11.48% of the total world's landmass"),
         ('USA', 9372610, "USA is 6.29% of the total world's landmass"),
         ('Iran', 1648195, "Iran is 1.11% of the total world's landmass"))

for name, area, check in areas:
    print(area_of_country(name=name, area=area) == check)


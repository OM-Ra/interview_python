# -*- coding: utf-8 -*-

'''
В холода мы носим многослойную одежду (майка, рубашка, свитер, пальто и т. п.).
Предположим, что каждый слой одежды повышает температуру окружающей среды
вокруг нашего тела на 0,1 текущей температуры на улице.

Напишите функцию, которая будет принимать число слоев одежды (n)
и температуру окружающей среды и возвращать итоговую температуру под всей этой одеждой.

Примечания:

- Результат округляем до десятых.
- Температура будет указываться в градусах Цельсия и в виде строки.
Она будет только положительной.
- Обратите внимание, что в качестве символа градуса используется звёздочка.

Примеры:

calc_bundled_temp(2, "10*C") "12.1*C"
# 10 * 1.1 = 11
# 11 * 1.1 = 12.1

calc_bundled_temp(1, "2*C") "2.2*C"
calc_bundled_temp(4, "6*C") "8.8*C"
calc_bundled_temp(20, "4*C") "26.9*C"
'''

def calc_bundled_temp(count_clothes: int, temperature: str) -> str:
    # Получение температуры.
    temperature = float(temperature.split('*')[0])
    # Проход по количеству одежды.
    for _ in range(count_clothes):
        # Увеличение температуры.
        temperature *= 1.1

    # Поулчение результата и его возврат.
    return f'{round(temperature, 1)}*C'


# Тесты.
tests =(
    ((2, "10*C"), "12.1*C"),
    ((1, "2*C"), "2.2*C"),
    ((4, "6*C"), "8.8*C"),
    ((20, "4*C"), "26.9*C")
)

for index, item in enumerate(tests):
    res = calc_bundled_temp(*item[0])
    assert res == item[1], f'tests:{index:>02} >>> {item[0]} -> {res} != {item[1]}'

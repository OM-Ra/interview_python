# -*- coding: utf-8 -*-

'''
Напишите функцию, которая будет принимать число
и возвращать его в виде денежной суммы
в долларах (и центах) США.

Примечания
- Нужно обязательно округлять дробную часть
числа до сотых. Обратите внимание, что дробная
часть числа в денежном формате отделяется точкой,
а тысячи разделяются запятыми.

- В функцию могут передаваться как положительные,
так и отрицательные числа.

Примеры
dolla_dolla_bills(10)           "$10.00"
dolla_dolla_bills(1000000)      "$1,000,000.00"
dolla_dolla_bills(-314159.2653) "-$314,159.27"
dolla_dolla_bills(-56.99)       "-$56.99"
'''

def dolla_dolla_bills(nbr: float) -> str:
    '''
    Преобразовывает число nbr в строку содержащую
    денежное представление этого числа в долларах
    и центах.
    '''
    # Воспользовавшись свойствами форматирования
    # получаем нужную строку.
    return f'${nbr:,.2f}'.replace('$-', '-$')



tests = ((10, "$10.00"),
         (1000000, "$1,000,000.00"),
         (-314159.2653, "-$314,159.27"),
         (-56.99, "-$56.99"))

for nbr, check in tests:
    print(dolla_dolla_bills(nbr=nbr) , check)


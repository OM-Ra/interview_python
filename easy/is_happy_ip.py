# -*- coding: utf-8 -*-

'''
Найти «счастливый» ip. Он считается счастливым,
если сумма двух байтов с левой стороны равняются
сумме двух байтов с правой стороны.

На вход функции всегда идёт строка с ipv4 адресом.

Пример:
is_happy_ip("255.255.255.255") -> True
is_happy_ip("0.0.0.1") -> False
is_happy_ip("101.78.170.9") -> True
'''

def is_happy_ip(ip: str) -> bool:
    '''
    Сравнивает суммы правых двух байтов
    с суммой левых двух байтов.
    '''
    ip = list(map(int, ip.split('.')))
    return sum(ip[:2]) == sum(ip[2:])



arr_ip = (("255.255.255.255", True),
          ("0.0.0.1", False),
          ("101.78.170.9", True))

for ip, check in arr_ip:
    print(is_happy_ip(ip=ip) == check)

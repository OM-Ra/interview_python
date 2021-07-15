# -*- coding: utf-8 -*-

'''
На вход идёт словарик типа «Монета : Количество».
Монеты могут быть 1, 3, 5 и 10 рублёвыми.
Количество монет и цена товара не ограничивается.

Метод находит суму всех монет и сравнивает цену.
Если пользователь может себе позволить товар,
то возвращает True, иначе — False.

Пример:

moneys = {5: 2, 3 : 2, 1 : 10, 10 : 0}  # sum - 26

is_can_buy(moneys, 27) → False
is_can_buy(moneys, 36) → False
is_can_buy(moneys, 26) → True
is_can_buy(moneys, 15) → True
'''

def is_can_buy(coins: dict, price: int) -> bool:
    '''
    Функция возвращает True если монет меньше или равно price,
    иначе False.

    price - цена покупки. Это сравниваемое значение.

    coins - словарь с номиналом монет и их количеством.
    '''
    # Для определения количества монет по значениям словаря
    # coin - номинал и nbr - количество монет
    func = lambda coin, nbr: coin * nbr
    res = map(func, coins.keys(), coins.values())
    return sum(res) >= price



moneys = {5: 2, 3: 2, 1: 10, 10: 0} # sum 26
prices = ((27, False), (36, False), (26, True), (15, True))

for price, check in prices:
    print(is_can_buy(coins=moneys, price=price) == check)


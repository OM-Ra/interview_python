# -*- coding: utf-8 -*-

'''
Сделайте так, чтобы число секунд отображалось в формате:
дни:часы:минуты:секунды.
'''
MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

def consider_time(sec: int) -> str:
    '''
    Переводит количество секунд в формат:
    ДНИ:ЧАСЫ:МИНУТЫ:СЕКУНДЫ.
    '''
    day = divmod(sec, DAY)
    hour = divmod(day[1], HOUR)
    minute = divmod(hour[1], MINUTE)
    return f'{day[0]:0>2d}:{hour[0]:0>2d}:{minute[0]:0>2d}:{minute[1]:0>2d}'



times = ((120, '00:00:02:00'),
         (3600, '00:01:00:00'),
         (86400, '01:00:00:00'),
         (90153, '01:01:02:33'),
         (6851561, '79:07:12:41'))

for sec, check in times:
    print(consider_time(sec=sec) == check)


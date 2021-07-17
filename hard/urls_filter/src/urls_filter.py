# -*- coding: utf-8 -*-

from sys import stderr
from os import path, remove
from collections import Counter

from settings import BYTES

from typing import List

class URLFilter:

    def __init__(self, arr_file: List[str], count_mem: int) -> None:
        '''
        arr_file - содержит список с именами файлов в которых
                   лежат url-адреса.
        work_mem - количество рабочей оперативной памяти в
                   указывается в гигабайтах, но хранится в байтах.
        '''
        self.arr_file = arr_file
        self.new_file = list()
        self.work_mem = count_mem * BYTES

    def check_file(self, file_name: str) -> bool:
        '''Проверяет существование файла.'''
        return path.isfile(file_name)

    def write_urls(self, file_name: str, count_urls: dict) -> None:
        '''Создаёт файл и записывает в него адреса.'''
        with open(file_name, 'w') as fd:
            fd.writelines(count_urls.keys())

    def create_new_file(self, file_name: str, nbr_file: int) -> int:
        '''
        Создаётся новое имя файла, и проверяется, чтобы
        такого имени файла уже небыло.
        Возвращается обновлённый счётчик файлов nbr_file.
        '''
        while self.check_file(f'{file_name}_filter{nbr_file}'):
            nbr_file += 1
        self.new_file.append(f'{file_name}_filter{nbr_file}')
        return nbr_file + 1

    def read_one_file(self, file_name: str) -> dict:
        '''
        Читает адреса из одного файла и возвращает словарь
        типа Counter считанных адресов.
        '''
        with open(file_name, 'r') as fd:
            return Counter(fd.readlines())

    def remove_dublicate(self, tmp_urls: dict) -> None:
        '''Удаляет адреса которые являются дубликатом.'''
        for url, value in tmp_urls.most_common():
            if value != 1: del tmp_urls[url]

    def remove_empty_file(self) -> None:
        '''Удаляет новые файлы которые пусты.'''
        for file_name in self.new_file:
            if not path.getsize(file_name):
                remove(file_name)

    def remove_file_and_replace(self,
                                tmp_file_name: str,
                                tmp_urls: dict,
                                urls_file_name: dict) -> None:
        '''
        Удаляет файл с дубликатами адресов.
        Затем, записывает адреса в файл с таким же названием.
        '''
         # Удаление файла с дубликатами
        remove(tmp_file_name)
        # Удаляем дубликаты
        self.remove_dublicate(tmp_urls=tmp_urls)
        # Вычетаем адреса которые содержатся в другом файле
        tmp_urls.subtract(urls_file_name)
        # Удаляем адреса которые находятся в другом файле
        self.remove_dublicate(tmp_urls=tmp_urls)
        # Запись адресов без дубликатов
        self.write_urls(file_name=tmp_file_name, count_urls=tmp_urls)

    def go_filter_1(self) -> None:
        '''Запуск фильтрации url-адресов.'''
        # Проходим по всем исходным файлам
        for file_name in self.arr_file:
            if not self.check_file(file_name=file_name): continue
            with open(file_name, 'r') as fd:
                nbr_file = 1 # Переменная для создания нового и оригинального имени файла
                # Считываем
                while tmp_urls := Counter(fd.readlines(self.work_mem // 2)):
                    # Создаётся имя нового файла
                    nbr_file = self.create_new_file(file_name=file_name, nbr_file=nbr_file)
                    # Записываем отфильтрованные данные
                    self.write_urls(file_name=self.new_file[-1], count_urls=tmp_urls)

    def go_filter_2(self) -> None:
        '''
        Теперь идёт поиск дубликатов по всем новым файлам и
        их удаление.
        '''
        # Начинаем проходить по всем новым файлам не включая последний
        for index, file_name in enumerate(self.new_file[:-1]):
            # Считываем адреса
            urls_file_name = self.read_one_file(file_name=file_name)
            # Проходим по всем файлам не включая уже пройденные выше и
            # не включая текущий файл
            for tmp_file_name in self.new_file[index + 1:]:
                # Считываем данные из файла
                tmp_urls = self.read_one_file(file_name=tmp_file_name)
                # Складываем значения из двух файлов
                tmp_urls.update(urls_file_name)
                # Делаем проверку на наличие дубликатов
                if tmp_urls and tmp_urls.most_common(1)[0][1] > 1:
                    # Удаляем дубликаты, файл tmp_file_name с дубликатами, а затем
                    # записываем в новый файл с таким же именем как и у tmp_file_name
                    # адреса которых нет в файле file_name
                    self.remove_file_and_replace(tmp_file_name=tmp_file_name,
                                                 tmp_urls=tmp_urls,
                                                 urls_file_name=urls_file_name)

    def go(self) -> None:
        '''
        Метод для запуска всего процесса.
        Адреса будут отфильтрованы от дубликатов.
        Новые созданные фпйлы которые останутся пустыми
        будут удалены.
        '''
        self.go_filter_1()
        self.go_filter_2()
        self.remove_empty_file()


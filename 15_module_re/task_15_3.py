#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию parse_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import readline
import re

f1=input('File:')
if not f1:
    f1='config_r1.txt'

def parse_cfg(f2):
    result=[]
    with open(f2, 'r') as f:
        for line in f:
            match = re.search('ip address '
                              '(\d*\.\d*\.\d*\.\d*) '
                              '(\d*\.\d*\.\d*\.\d*)',line)
            if match:
                result.append(match.group(1,2))
    return result
print(parse_cfg(f1))
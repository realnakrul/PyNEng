#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''
import readline
import re
from pprint import pprint
f1=input('File:')
if not f1:
    f1='sh_ip_int_br_2.txt'
print(f1)

def parse_sh_ip_int_br(f2):
    result=[]
    with open(f2, 'r') as f:
        for line in f:
            match = re.search('(\S+) +'
                              '(\S+) +'
                              '\w+ +\w+ +'
                              '(up|down|administratively down) +'
                              '(up|down)',line)
            if match:
                result.append(match.groups())
    return result
pprint(parse_sh_ip_int_br(f1))
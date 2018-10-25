#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import readline
import re
from pprint import pprint
f1=input('File:')
if not f1:
    f1='config_r1.txt'
print(f1)

def parse_cfg(f2):
    result={}
    with open(f2, 'r') as f:
        for line in f:
            match_intf = re.search('interface (\S*)',line)
            if match_intf:
                intf=match_intf.group(1)
            match_ip = re.search('ip address '
                              '(\d*\.\d*\.\d*\.\d*) '
                              '(\d*\.\d*\.\d*\.\d*)',line)
            if match_ip:
                result.update({intf:match_ip.group(1,2)})
    return result
pprint(parse_cfg(f1))
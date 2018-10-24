#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 15.1c

Проверить работу скрипта из задания 15.1 и регулярного выражения из задания 15.1a или 9.1b
на выводе sh ip int br из файла sh_ip_int_br_switch.txt.

Если, в результате выполнения скрипта, были выведены не только строки
с интерфейсами 0/1 и 0/3, исправить регулярное выражение.
В регулярном выражении по-прежнему должно быть не более 7 символов.

В результате, должны выводиться только строки с интерфейсами 0/1 и 0/3.

В этом файле нужно написать только регулярное выражение.

'''

regex = '0 |3 '
import readline
import re

f1=input('File:')
r1=input('Regex:')
if not f1:
    f1='sh_ip_int_br_switch.txt'
if not r1:
    r1=regex

def regf(f2,r2):
    with open(f2, 'r') as f:
        r2='.*('+r2+').*'
        print(r2)
        for line in f:
            match = re.search(r2,line)
            if match:
                print(match.group(0))
regf(f1,r1)
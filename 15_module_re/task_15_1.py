#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 15.1

Создать скрипт, который будет ожидать два аргумента:
1. имя файла, в котором находится вывод команды show
2. регулярное выражение

В результате выполнения скрипта, на стандартный поток вывода должны быть
выведены те строки из файла с выводом команды show,
в которых было найдено совпадение с регулярным выражением.

Проверить работу скрипта на примере вывода команды sh ip int br (файл sh_ip_int_br.txt).
Например, попробуйте вывести информацию только по интерфейсу FastEthernet0/1.

Работа этого скрипта должна имитировать работу фильтра include в Cisco.
Пример работы скрипта:

$ python task_9_1.py sh_ip_int_br.txt "Fas"
FastEthernet0/0            15.0.15.1       YES manual up                    up
FastEthernet0/1            10.0.12.1       YES manual up                    up
FastEthernet0/2            10.0.13.1       YES manual up                    up
FastEthernet0/3            unassigned      YES unset  up                    down

$ python task_9_1.py sh_ip_int_br.txt "manual"
FastEthernet0/0            15.0.15.1       YES manual up                    up
FastEthernet0/1            10.0.12.1       YES manual up                    up
FastEthernet0/2            10.0.13.1       YES manual up                    up
Loopback0                  10.1.1.1        YES manual up                    up
Loopback100                100.0.0.1       YES manual up                    up

$ python task_9_1.py sh_ip_int_br.txt "up +up"
FastEthernet0/0            15.0.15.1       YES manual up                    up
FastEthernet0/1            10.0.12.1       YES manual up                    up
FastEthernet0/2            10.0.13.1       YES manual up                    up
Loopback0                  10.1.1.1        YES manual up                    up
Loopback100                100.0.0.1       YES manual up                    up

'''

import readline
import re

f1=input('File:')
r1=input('Regex:')
if not f1:
    f1='sh_ip_int_br.txt'
if not r1:
    r1='Fas'

def regf(f2,r2):
    with open(f2, 'r') as f:
        r2='.*('+r2+').*'
        print(r2)
        for line in f:
            match = re.search(r2,line)
            if match:
                print(match.group(0))
regf(f1,r1)

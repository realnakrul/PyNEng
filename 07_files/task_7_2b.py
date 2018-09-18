#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
cfg_lines=[]
ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
fname = argv[1]
with open(argv[1], 'r') as f:
    for line in f:
        ignore_condition=''
        for i in ignore:
            if i in line:
                ignore_condition=i
        if not ignore_condition:
            cfg_lines.append(line.rstrip()+'\n')
print(cfg_lines)
f = open('config_sw1_cleared.txt', 'w')
f.writelines(cfg_lines)
f.close()

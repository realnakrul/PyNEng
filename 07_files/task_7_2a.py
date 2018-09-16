#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
fname = argv[1]
print(fname)
with open(argv[1], 'r') as f:
    for line in f:
        if not line.startswith('!'):
            ignore_condition=''
            for i in ignore:
                if i in line:
                    ignore_condition=i
            if not ignore_condition:
                print(line.rstrip())

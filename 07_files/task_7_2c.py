#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
cfg_lines=[]
ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
fname_in = argv[1]
fname_out = argv[2]
with open(fname_in, 'r') as f:
    for line in f:
        ignore_condition=''
        for i in ignore:
            if i in line:
                ignore_condition=i
        if not ignore_condition:
            cfg_lines.append(line.rstrip()+'\n')
print(cfg_lines)
f = open(fname_out, 'w')
f.writelines(cfg_lines)
f.close()

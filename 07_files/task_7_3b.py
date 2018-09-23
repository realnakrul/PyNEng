#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
import readline
vlan=input('Enter VLAN number: ')
template=''' {}    {}   {}'''
with open('CAM_table.txt', 'r') as f:
    for line in f:
        content=line.rstrip().split()
        if len(content)==4 and content[0] == vlan:
            print(template.format(content[0],content[1], content[3]))

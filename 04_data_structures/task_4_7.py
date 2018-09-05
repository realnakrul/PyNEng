#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
OCTETS=MAC.split(':')
OCTETS[0]=int(OCTETS[0],16)
OCTETS[1]=int(OCTETS[1],16)
OCTETS[2]=int(OCTETS[2],16)
print('{:016b} {:016b} {:016b}'.format(OCTETS[0], OCTETS[1], OCTETS[2]))

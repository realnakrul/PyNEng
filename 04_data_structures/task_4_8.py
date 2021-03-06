#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1'
PARTS=IP.split('.')
PARTS[0]=int(PARTS[0])
PARTS[1]=int(PARTS[1])
PARTS[2]=int(PARTS[2])
PARTS[3]=int(PARTS[3])
IP_TEMPLATE='''
{O1:<8}  {O2:<8}  {O3:<8}  {O4:<8}
{O1:08b}  {O2:08b}  {O3:08b}  {O4:08b}
'''
print(IP_TEMPLATE.format(O1=PARTS[0], O2=PARTS[1], O3=PARTS[2],
O4=PARTS[3]))

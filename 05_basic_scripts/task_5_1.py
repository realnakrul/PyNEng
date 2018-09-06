#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import readline
SUBNET_FULL=input('Enter subnet in following format 10.1.1.0/24: ').split('/')
IP=SUBNET_FULL[0].split('.')
IP[0]=int(IP[0])
IP[1]=int(IP[1])
IP[2]=int(IP[2])
IP[3]=int(IP[3])
SUBNET_FULL[1]=int(SUBNET_FULL[1])
M="1"*SUBNET_FULL[1]+"0"*(32-SUBNET_FULL[1])
M1=int(M[:8],2)
M2=int(M[8:16],2)
M3=int(M[16:24],2)
M4=int(M[24:],2)
OUT_TEMPLATE='''

Network:
{O1:<8}  {O2:<8}  {O3:<8}  {O4:<8}
{O1:08b}  {O2:08b}  {O3:08b}  {O4:08b}

Mask:
/{M}
{M1:<8}  {M2:<8}  {M3:<8}  {M4:<8}
{M1:08b}  {M2:08b}  {M3:08b}  {M4:08b}
'''
print(OUT_TEMPLATE.format(O1=IP[0],O2=IP[1],O3=IP[2],O4=IP[3],M=SUBNET_FULL[1],M1=M1,M2=M2,M3=M3,M4=M4))

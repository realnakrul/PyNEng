#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import readline
RESULT=''
RANGE_COUNTER=0
while not RESULT:
    IP=input('Enter IP address: ').split('.')
    if len(IP)==4:
        #STR to INT conversion
        for OCTET in range(len(IP)):
            try:
                IP[OCTET]=int(IP[OCTET])
                if IP[OCTET]>=0 and IP[OCTET]<=255:
                    RANGE_COUNTER+=1
            except:
                RANGE_COUNTER=0
    if RANGE_COUNTER < 4:
        print('Incorrect IPv4 address')
    else:
        RESULT='unused'
if IP[0]==255 and IP[1]==255 and IP[2]==255 and IP[3]==255:
    RESULT='local broadcast'
elif IP[0]==0 and IP[1]==0 and IP[2]==0 and IP[3]==0:
    RESULT='unassigned'
elif IP[0]>=1 and IP[0]<=223:
    RESULT='unicast'
elif IP[0]>=224 and IP[0]<=239:
    RESULT='multicast'
print(RESULT)

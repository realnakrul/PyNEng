#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
import readline
RANGE_COUNTER=0
IP=input('Enter IP address: ').split('.')
#STR to INT conversion
for OCTET in range(len(IP)):
	try:
		IP[OCTET]=int(IP[OCTET])
		if IP[OCTET]>=0 and IP[OCTET]<=255:
			RANGE_COUNTER+=1
	except:
		RANGE_COUNTER=0
if len(IP)!=4 or RANGE_COUNTER!=4:
    RESULT='Incorrect IPv4 address'
elif IP[0]==255 and IP[1]==255 and IP[2]==255 and IP[3]==255:
    RESULT='local broadcast'
elif IP[0]==0 and IP[1]==0 and IP[2]==0 and IP[3]==0:
    RESULT='unassigned'
elif IP[0]>=1 and IP[0]<=223:
    RESULT='unicast'
elif IP[0]>=224 and IP[0]<=239:
    RESULT='multicast'
else:
    RESULT='unused'
print(RESULT)

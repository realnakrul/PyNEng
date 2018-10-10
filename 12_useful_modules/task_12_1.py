#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess

iptocheck=['192.168.148.128', '192.168.148.1', '192.168.148.129']

def check_ip_addresses(iplist):
    ipavailable=[]
    ipbusy=[]
    for i in iplist:
        print('Trying ',i,'...')
        reply = subprocess.run(['ping', '-c', '3', i], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        if reply.returncode == 0:
            ipbusy.append(i)
        else:
            ipavailable.append(i)
    return ipbusy, ipavailable

print(check_ip_addresses(iptocheck))

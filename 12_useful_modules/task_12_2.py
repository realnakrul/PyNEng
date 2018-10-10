#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''
import subprocess
import ipaddress

iptocheck=['192.168.148.1', '192.168.148.10-192.168.148.11', '192.168.148.12-18', '192.168.148.128']

def check_ip_addresses(iplist):
    ipavailable=[]
    ipbusy=[]
    for i in iplist:
        print('Trying',i,'...')
        reply = subprocess.run(['ping', '-c', '3', i], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        if reply.returncode == 0:
            ipbusy.append(i)
        else:
            ipavailable.append(i)
    return ipbusy, ipavailable

def ipdecode(iplist):
    ipdecoded=[]
    decodefail=[]
    for i in iplist:
        try:
            ipaddress.ip_address(i)
            ipdecoded.append(i)
        except ValueError:
            decodefail.append(i)
    if decodefail:
        for i_fail in decodefail:
            i_first,i_last=i_fail.split('-')
            *base,i_first=i_first.split('.')
            i_last=i_last.split('.')[-1]
            i_res=''
            for gen in range(int(i_first),int(i_last)+1):
                try:
                    i_res='.'.join([str(oct) for oct in base])+'.'+str(gen)
                    ipaddress.ip_address(i_res)
                    ipdecoded.append(i_res)
                except ValueError:
                    pass
    return ipdecoded

iptocheck=ipdecode(iptocheck)
print(iptocheck)
print(check_ip_addresses(iptocheck))

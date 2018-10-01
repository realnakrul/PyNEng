#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(conf):
    result_access = {}
    result_trunk = {}
    int_start=False
    with open(conf) as f:
        for line in f:
            if line.startswith('interface'):
                int_name = line.split()[-1]
                int_start=True
            elif '!' in line:
                int_start=False
            elif int_start == True and 'access vlan' in line:
                vlan=line.split()[-1]
                result_access.update({int_name:vlan})
            elif int_start == True and 'allowed vlan' in line:
                vlan = line.split()[-1].split(',')
                vlan = [int(vl_str) for vl_str in vlan]
                result_trunk.update({int_name:vlan})
    return result_access,result_trunk
print(get_int_vlan_map('config_sw1.txt'))

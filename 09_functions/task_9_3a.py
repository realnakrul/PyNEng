#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif int_start == True and 'mode access' in line:
                vlan=1
                result_access.update({int_name:vlan})
            elif int_start == True and 'access vlan' in line:
                vlan=int(line.split()[-1])
                result_access.update({int_name:vlan})
            elif int_start == True and 'allowed vlan' in line:
                vlan = line.split()[-1].split(',')
                vlan = [int(vl_str) for vl_str in vlan]
                result_trunk.update({int_name:vlan})
    return result_access,result_trunk
print(get_int_vlan_map('config_sw2.txt'))

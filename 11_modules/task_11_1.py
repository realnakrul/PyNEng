#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def parse_cdp_neighbors(cdp_output):
    result={}
    for line in cdp_output.split('\n'):
        if 'show cdp neighbors' in line:
            dev_a=line.split('>')[0]
        if 'Eth' in line:
            dev_b=line.split()[0]
            int_a=line.split()[1]+line.split()[2]
            int_b=line.split()[-2]+line.split()[-1]
            result.update({tuple([dev_a,int_a]):tuple([dev_b,int_b])})
    return result

if __name__ == "__main__":
    with open('sw1_sh_cdp_neighbors.txt', 'r') as f:
        print(parse_cdp_neighbors(f.read()))

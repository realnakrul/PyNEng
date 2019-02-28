#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''


def parse_sh_cdp_neighbors(cdp_string):
    """Parses sh cdp neighbors """
    import re
    cdp_list = cdp_string.split('\n')
    neighbor_dict = []
    for line in cdp_list:
        parent_dev_re = re.search('^(\S+)>', line)
        neighbor_dev_re = re.search('^(\S+) +(\S+ \S+).+ (\S+ \S+\d)$', line)  # Three groups, last ends with digit
        if parent_dev_re:
            parent_dev_id = parent_dev_re.group(1)
            neighbor_dict = {parent_dev_id: {}}
        if neighbor_dev_re:
            neighbor_dev_id = neighbor_dev_re.group(1)
            parent_dev_int = neighbor_dev_re.group(2)
            neighbor_dev_int = neighbor_dev_re.group(3)
            neighbor_dict[parent_dev_id][parent_dev_int] = {neighbor_dev_id: neighbor_dev_int}
    return neighbor_dict


if __name__ == '__main__':
    from pprint import pprint
    with open('sh_cdp_n_sw1.txt', 'r') as f:
        show_out = f.read().rstrip()
    pprint(parse_sh_cdp_neighbors(show_out))

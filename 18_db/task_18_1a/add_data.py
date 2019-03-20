#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''


def parse_dhcp_file(dhcp_file):
    import re
    result = []
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    with open(dhcp_file) as data:
        sw_name, *_ = dhcp_file.split('_')
        for line in data:
            match_list = []
            match = regex.search(line)
            if match:
                match_list = list(match.groups())
                match_list.append(sw_name)
                result.append(tuple(match_list))
    return result


def parse_yml_file(sw_yml_file):
    import yaml
    sw_data_list = []
    with open(sw_yml_file) as f:
        switches_data = yaml.load(f)
    for s in switches_data['switches'].keys():
        sw_data_list.append((s, switches_data['switches'][s]))
    return sw_data_list


def add_data(connection, dhcp_data_list, sw_data_list):
    import sqlite3
    for row in dhcp_data_list:
        try:
            with connection:
                query = '''insert into dhcp (mac, ip, vlan, interface, switch)
                           values (?, ?, ?, ?, ?)'''
                connection.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)
    for row in sw_data_list:
        try:
            with connection:
                query = '''insert into switches (hostname, location)
                           values (?, ?)'''
                connection.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)


if __name__ == '__main__':
    import glob
    from pprint import pprint
    dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
    print(dhcp_snoop_files)
    dhcp_list = []

    for sw_file in dhcp_snoop_files:
        dhcp_list.extend(parse_dhcp_file(sw_file))

    print(dhcp_list)
    print('Inserting DHCP Snooping data')

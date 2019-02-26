#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает

Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''


def file_read(file_name):
    """Reads file content into list and extracts device host name"""
    *_, host_name = file_name[:file_name.find('.')].split('_')
    with open(file_name, 'r') as file1:
        show_out = file1.read().rstrip().split('\n')
    return host_name, show_out


def parse_sh_version(output):
    import re
    for line in output:
        if line.startswith('Cisco IOS Software'):
            ios = re.search('Version (\S+),', line)
        if line.startswith('router uptime'):
            uptime = re.search('is (.+)', line)
        if line.startswith('System image'):
            image = re.search('is "(.+)"', line)
    return ios.group(1), image.group(1), uptime.group(1)


def write_to_csv(file_output,data_output):
    with open(file_output, 'w') as f:
        writer = csv.writer(f)
        for row in data_output:
            writer.writerow(row)


if __name__ == '__main__':
    import glob
    import csv
    # from pprint import pprint
    sh_version_files = glob.glob('sh_vers*')
    print(sh_version_files)
    headers = ['hostname', 'ios', 'image', 'uptime']
    main_output = []
    main_output.append(headers)
    for f in sh_version_files:
        main_host_name, main_content = (file_read(f))
        main_output.append([main_host_name]+list(parse_sh_version(main_content)))
    write_to_csv('task_17_1.csv', main_output)

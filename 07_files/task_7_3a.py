#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
mega=[]
sorted = False
template=''' {}    {}   {}'''
#reading from file
with open('CAM_table.txt', 'r') as f:
    for line in f:
        content=line.rstrip().split()
        if len(content)==4 and content[0] != '----':
            mega.append(list((int(content[0]),content[1],content[3])))
#sorting
while not sorted:
    flag=True
    for i in range(len(mega)-1):
        if mega[i][0] > mega[i+1][0]:
            temp=mega[i]
            mega[i]=mega[i+1]
            mega[i+1]=temp
            flag=False
    sorted=flag
#results output
for i in range(len(mega)):
    print(template.format(mega[i][0],mega[i][1],mega[i][2]))

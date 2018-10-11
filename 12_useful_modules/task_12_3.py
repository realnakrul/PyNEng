#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
from tabulate import tabulate
list1=['10.1.1.1', '10.1.1.2']
list2=['10.1.1.7', '10.1.1.8', '10.1.1.8']
def ip_table(reach, unreach):
    col=['Reachable','Unreachable']
    list3=[]
    m1=max(len(reach),len(unreach))
    for i in range(m1):
        a=''
        b=''
        try:
            a=reach[i]
        except IndexError:
            pass
        try:
            b=unreach[i]
        except IndexError:
            pass
        list3.append([a,b])
    print(tabulate(list3, headers=col))
ip_table(list1,list2)
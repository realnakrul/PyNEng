#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ROUTE_PROP=ospf_route.split()
ROUTE_PROP[0]=ROUTE_PROP[0].replace('O', 'OSPF')
ROUTE_PROP[4]=ROUTE_PROP[4].strip(',')
ROUTE_PROP[5]=ROUTE_PROP[5].strip(',')
RESULT_TEMPLATE='''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''
print(RESULT_TEMPLATE.format(ROUTE_PROP[0],ROUTE_PROP[1],ROUTE_PROP[2],ROUTE_PROP[4],ROUTE_PROP[5],ROUTE_PROP[6]))

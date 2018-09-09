#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''
import readline
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
INT_DICT={
'access': {
'request': 'Enter VLAN number: ',
'template': access_template
}, 
'trunk': {
'request': 'Enter allowed VLANs: ',
'template': trunk_template
}}
INT_MODE=input('Enter interface mode (access/trunk): ')
INT_NUM=input('Enter interface type and number: ')
VL=input(INT_DICT[INT_MODE]['request'])
print('\ninterface '+INT_NUM)
print('\n'.join(INT_DICT[INT_MODE]['template']).format(VL))

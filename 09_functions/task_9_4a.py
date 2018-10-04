#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration', '!']

def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)

def config_to_dict(conf):
    result={}
    block=[]
    command_high=''
    command_2=''
    new_block=False
    tripple=False
    with open(conf) as f:
        for line in f:
            line=line.rstrip()
            '''Cutting config to blocks. New block starts with string without sapce and
            check tripple depth for the block'''
            if line and not check_ignore(line, ignore):
                if line[0]!=' ':
                    old_block=block
                    block=[]
                    new_block=True
                else:
                    new_block=False
                    if line.startswith('  '):
                        tripple=True                   
                block.append(line)
                '''Parse block Depends on depth '''
                if new_block:
                    if tripple:
                    	for str in old_block:
                            if str[0]!=' ':
                                result.update({str:{}})
                                command_high=str
                            else:
                                str=str[1:]
                                if str[0]!=' ':
                                    result[command_high].update({str:[]})
                                    command_2=str
                                else:
                                    result[command_high][command_2].append(str.strip())
                    else:
                        for str in old_block:
                            if str[0]!=' ':
                                result.update({str:[]})
                                command_high=str
                            else:
                                result[command_high].append(str.strip())
                    tripple=False
        return result
parse=config_to_dict('config_r1.txt')
for key in parse.keys():
    print('\n'+key)
    if type(parse[key])==type(dict()):
        for sub_key in parse[key].keys():
            print('    '+sub_key)
            print('        '+str(parse[key][sub_key]))
    else:
        print('    '+str(parse[key]))
    

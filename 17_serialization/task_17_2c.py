#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''


def neighbors_dedup(neighbors_dict):
    """Removes duplicate connections from neighbors dictionary"""
    neighbors_dict_dedup = {}
    for n1 in neighbors_dict.keys():
        duplicate_flag = False
        for n2 in neighbors_dict_dedup.keys():
            if (n1 == n2) or (n1 == neighbors_dict_dedup[n2]):
                duplicate_flag = True
        if not duplicate_flag:
            neighbors_dict_dedup.update({n1: neighbors_dict[n1]})
    return neighbors_dict_dedup


if __name__ == '__main__':
    import yaml
    from pprint import pprint
    from draw_network_graph import draw_topology
    with open('topology.yaml') as f:
        topology_old = yaml.load(f)
    topology_new = {}
    for k1 in topology_old.keys():
        for k2 in topology_old[k1].keys():
            local_dev = (k1, k2)
            for k3 in topology_old[k1][k2].keys():
                remote_dev = (k3, topology_old[k1][k2][k3])
                topology_new.update({local_dev: remote_dev})
    neighbors_dedup(topology_new)
    draw_topology(neighbors_dedup(topology_new))
    pprint(topology_new)
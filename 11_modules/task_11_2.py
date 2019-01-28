#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 11.2

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor в файле sw1_sh_cdp_neighbors.txt

Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
import draw_network_graph

import task_11_1


with open('sw1_sh_cdp_neighbors.txt') as f:	
		l2_map_dict = task_11_1.parse_cdp_neighbors(f.read().strip())

draw_network_graph.draw_topology(l2_map_dict)


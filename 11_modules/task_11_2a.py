#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


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


list_files = ['sh_cdp_n_sw1.txt',
			'sh_cdp_n_r1.txt',
			'sh_cdp_n_r2.txt',
			'sh_cdp_n_r3.txt',]

l2_map_dict = {}
for file in list_files:
	with open(file) as f:	
		new_dict = task_11_1.parse_cdp_neighbors(f.read().strip())
	for n_key,n_val in new_dict.items():
		if not any(key == n_val for key in l2_map_dict.keys()):
			l2_map_dict[n_key] = n_val
		
		

draw_network_graph.draw_topology(l2_map_dict)

#for k,v in l2_map_dict.items():
#	print(k,v,sep=' : ')




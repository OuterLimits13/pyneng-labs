#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 17.2a

С помощью функции parse_sh_cdp_neighbors из задания 17.2,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Не копировать код функции parse_sh_cdp_neighbors
'''


from pprint import pprint
import re
import glob
import yaml

def parse_sh_cdp_neighbors(output):
	output = output.strip().split('\n')
	dev_l2_map = {}
	for line in output:
		if '/' in line:
			r_dev, l_intf_type, l_intf_port, *other, r_intf_type,r_intf_port = line.split()
			dev_l2_map[device_name][l_intf_type + l_intf_port] = {r_dev : r_intf_type + r_intf_port}
			continue
		
		if 'cdp ne' in line:
			device_name = re.match('(\S+)[#>]',line)[1]
			dev_l2_map[device_name] = {}
					
	
	return dev_l2_map
	
	
list_of_files = glob.glob('sh_cdp*')	
list_of_files.sort()

topology = {}
for file_to_open in list_of_files:
	with open (file_to_open) as f:
		device_l2_connections = parse_sh_cdp_neighbors(f.read())
		topology.update(device_l2_connections)

with open('topology.yaml','w') as f:
	yaml.dump(topology,f)
	print('Файл записан ''topology.yaml')

#pprint(topology)















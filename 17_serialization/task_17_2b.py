#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 17.2b

Переделать функциональность скрипта из задания 17.2a,
в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
 * значение по умолчанию - True
* topology_filename - имя файла, в который сохранится топология.
 * по умолчанию, должно использоваться имя topology.yaml.
 * топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию.
Словарь должен быть в том же формате, что и в задании 17.2a.

Проверить работу функции generate_topology_from_cdp на файлах:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.

Не копировать код функции parse_sh_cdp_neighbors
'''

from pprint import pprint
import re
import glob
import yaml

def parse_sh_cdp_neighbors(output):
	'''
	обрабатывает вывод команды show cdp neighbors.

	Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
	Функция должна возвращать словарь, который описывает соединения между устройствами.

	пример словаря:
	{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
			'Fa0/2': {'R6': 'Fa0/0'}}}
	'''
	
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

def generate_topology_from_cdp(list_of_files,save_to_file=True,topology_filename='topology.yaml'):
	'''
	Функция generate_topology_from_cdp должна быть создана с параметрами:
	* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
	* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
	* topology_filename - имя файла, в который сохранится топология.
	 
	Функция возвращает словарь, который описывает топологию.
	'''
	topology = {}
	for file_to_open in list_of_files:
		with open (file_to_open) as f:
			device_l2_connections = parse_sh_cdp_neighbors(f.read())
			topology.update(device_l2_connections)

	if save_to_file:
		with open(topology_filename,'w') as f:
			yaml.dump(topology,f)
			print('Файл записан ' + topology_filename)
			
	return topology

	
	
if __name__ == "__main__":
	list_of_files = glob.glob('sh_cdp*')	
	list_of_files.sort()
	
	pprint( generate_topology_from_cdp(list_of_files) )
	






















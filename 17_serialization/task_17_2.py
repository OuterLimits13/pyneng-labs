#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

from pprint import pprint
import re

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
	
	
	
with open ('sh_cdp_n_sw1.txt') as f:
	device_l2_map = parse_sh_cdp_neighbors(f.read())
	
pprint(device_l2_map)



























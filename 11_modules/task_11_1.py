#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(sh_cdp_nei):
	sh_cdp_nei = sh_cdp_nei.split('\n')
	
	dict_l2_map = {}
	for line in sh_cdp_nei:
		if 'cdp nei' in line:
			from_device = line[:line.find('sh') - 1]
		if '/' in line:
			r_dev, l_intf_type, l_intf_port, *other, r_int_type,r_intf_port = line.split()
			dict_l2_map[(from_device,l_intf_type + l_intf_port)] = (r_dev,r_int_type + r_intf_port)
	
	return dict_l2_map
	
	
	
if __name__ == "__main__":
	with open('sw1_sh_cdp_neighbors.txt') as f:	
		result = parse_cdp_neighbors(f.read().strip())	
	print(result)
	


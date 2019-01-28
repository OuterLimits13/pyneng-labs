#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(file):
	'''
	Функция ожидает в качестве аргумента имя конфигурационного файла.
	
	Возвращает два объекта:
	1) словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
	2) словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
	'''
	with open(file) as f:
		sw_config_lines = f.read().rstrip().split('\n')
		

	trunk_dict, access_dict = {}, {}
	intf = ''
	for line in sw_config_lines:
		if 'Ethernet' in line and not intf:
			intf = line
			
		if 'access vlan' in line:
			access_dict[intf] = int(line.split()[-1])
		if 'trunk allowed' in line:
			trunk_dict[intf] = []
			[ trunk_dict[intf].append(int(vlan))  for  vlan  in  line.split()[-1].split(',') ]
					
		if '!' == line:
			intf = ''
		
		
	return trunk_dict, access_dict


trunk_dict, access_dict = get_int_vlan_map('config_sw1.txt')


print('\nTrunk interfaces:')
for intf, vlans in trunk_dict.items():
	print(intf,end=': ')
	print(*vlans,sep=', ') 
	
print('\nAccess interfaces:')
[ print(intf + ': ' + str(vlan)) for intf, vlan in access_dict.items() ]


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

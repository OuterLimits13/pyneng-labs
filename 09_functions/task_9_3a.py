#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
			
		if 'switchport mode access' in line:
			access_dict[intf] = 1
		if 'access vlan' in line:
			access_dict[intf] = int(line.split()[-1])
		if 'trunk allowed' in line:
			trunk_dict[intf] = []
			[ trunk_dict[intf].append(int(vlan))  for  vlan  in  line.split()[-1].split(',') ]
					
		if '!' == line:
			intf = ''
		elif 'interface Vlan' in line:
			break
					
	return trunk_dict, access_dict



trunk_dict, access_dict = get_int_vlan_map('config_sw2.txt')

print('\nTrunk interfaces:')
for intf, vlans in trunk_dict.items():
	print(intf,end=': ')
	print(*vlans,sep=', ') 
	
print('\nAccess interfaces:')
[ print(intf + ': ' + str(vlan)) for intf, vlan in access_dict.items() ]


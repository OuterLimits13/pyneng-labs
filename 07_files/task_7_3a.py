#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# solution
mac_table = []
with open('CAM_table.txt') as file:
	for line in file:
		if 'Gi' in line:
			line = line.replace('DYNAMIC    ','',).rstrip()
			mac_table.append(line)
			
mac_table.sort()
for mac_entry in mac_table:
	print(mac_entry)
	

#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# solution
mac_table = []

vlan = input('Введите номер vlan-a: ')
print('\nТаблица MAC-адресов для введенного vlan-а:')

with open('CAM_table.txt') as file:
	for line in file:
		if 'Gi' in line and line.startswith(' ' + vlan):
			line = line.replace('DYNAMIC    ','',).rstrip()
			print(line)
			


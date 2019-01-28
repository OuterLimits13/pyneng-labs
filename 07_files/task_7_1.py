#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# solution
with open('ospf.txt') as file:
	routes = file.read().rstrip().split('\n')

names = ['Protocol:', 'Prefix:','AD/Metric:','Next-Hop:','Last update:','Outbound Inteface:']

for route in routes:
	
	route = route.replace(',','').replace('via','').replace('[','').replace(']','').split() 
	for i in range(6):
		if route[i] == 'O':
			print('{:<21} OSPF'.format(names[i]))
		else:
			print('{:<21} {}'.format(names[i],route[i]))
	print('-'*20)

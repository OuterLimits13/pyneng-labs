#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
from tabulate import tabulate 


def ip_table(reacheble_list, unreacheble_list):
	'''
	Функция отображает таблицу доступных и недоступных IP-адресов. Функция ожидает как аргументы два списка:
	* список доступных IP-адресов
	* список недоступных IP-адресов
	Результат работы функции - вывод на стандартный поток вывода таблицы
	'''
		
	to_print = [('Reacheble', 'Unreacheble')]
	
	if len(reacheble_list) > len(unreacheble_list):
		temp_list = unreacheble_list.copy()
		while len(reacheble_list) > len(temp_list):
			temp_list.append('')
		[ to_print.append(x) for x in zip(reacheble_list,temp_list) ]
	elif len(reacheble_list) < len(unreacheble_list):
		temp_list = reacheble_list.copy()
		while len(temp_list) < len(unreacheble_list):
			temp_list.append('')
		[ to_print.append(x) for x in zip(temp_list, unreacheble_list) ]

		
	print(tabulate(to_print,headers='firstrow'))

	return



if __name__ == "__main__":
	reacheble_list = ['10.172.32.177', '10.172.32.179', '10.172.32.180']
	unreacheble_list = ['10.172.32.184', '10.172.32.185','10.172.32.199','10.172.32.198',]
	ip_table(reacheble_list, unreacheble_list)
	















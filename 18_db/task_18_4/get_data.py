#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 18.4

Обновить файл get_data из задания 18.2 или 18.2a.
Добавить поддержку столбца active, который мы добавили в задании 18.3.

Теперь, при запросе информации, сначала должны отображаться активные записи,
а затем, неактивные.

Например:
$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------

----------------------------------------
Inactive values:
----------------------------------------
mac         : 00:09:23:34:16:18
vlan        : 10
interface   : FastEthernet0/4
switch      : sw1
----------------------------------------

$ python get_data1.py
--------------------------------------------------------------------------------
Active values:
--------------------------------------------------------------------------------
00:09:BB:3D:D6:58  10.1.10.2         10    FastEthernet0/1    sw1         1
00:04:A3:3E:5B:69  10.1.5.2          5     FastEthernet0/10   sw1         1
00:05:B3:7E:9B:60  10.1.5.4          5     FastEthernet0/9    sw1         1
00:07:BC:3F:A6:50  10.1.10.6         10    FastEthernet0/3    sw1         1
00:09:BC:3F:A6:50  192.168.100.100   1     FastEthernet0/7    sw1         1
00:B4:A3:3E:5B:69  10.1.5.20         5     FastEthernet0/5    sw2         1
00:C5:B3:7E:9B:60  10.1.5.40         5     FastEthernet0/9    sw2         1
00:A9:BC:3F:A6:50  10.1.10.60        20    FastEthernet0/2    sw2         1
--------------------------------------------------------------------------------
Inactive values:
--------------------------------------------------------------------------------
00:A9:BB:3D:D6:58  10.1.10.20        10    FastEthernet0/7    sw2         0
'''

import sqlite3
import sys
from pprint import pprint
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
from tabulate import tabulate

def get_data(db_filename, key=None, value=None):
		
	conn = sqlite3.connect(db_filename)

	if key:
		keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
		#Позволяет далее обращаться к данным в колонках, по имени колонки
		conn.row_factory = sqlite3.Row
		
		keys.remove(key)
		print('\nDetailed information for host(s) with', key, value)
		print('-' * 40)

		query = 'select * from dhcp where {} = ? and active = 1'.format(key)
		result = conn.execute(query, (value, ))

		for row in result:
			for k in keys:
				print('{:12}: {}'.format(k, row[k]))
			print('-' * 40)
		
		query = 'select * from dhcp where {} = ? and active = 0'.format(key)
		result = conn.execute(query, (value, ))
		print('\n' + '=' * 40 + '\nInactive values:')
		for row in result:
			for k in keys:
				print('{:12}: {}'.format(k, row[k]))
			print('-' * 40)
		
	else:
		keys = ['mac', 'ip', 'vlan', 'interface', 'switch', 'active']
		print('\nВ таблице dhcp следующие записи:')
		print('-' * 60)		
		query = "select * from dhcp"
		result = conn.execute(query)
		result = result.fetchall()
		
		result_active, result_inactive = [],[]
		for row in result:
			if row[5]:
				result_active.append(row)
			else:
				result_inactive.append(row)
		print("Active values:\n" + '-' * 60)
		print(tabulate(result_active, headers=keys))
		print('-' * 60)		
		print("Inactive values:\n" + '-' * 60)
		print(tabulate(result_inactive, headers=keys))
				
			
	conn.close()
	return



db_filename = 'dhcp_snooping.db'
if len(sys.argv) == 3:
	key, value = sys.argv[1:]
	get_data(db_filename, key, value)
elif len(sys.argv) == 1:
	get_data(db_filename)
else:
	print("Ошибка! Введите ноль или два аргумента (имя столбца и значение)")
	









#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import glob
import sqlite3
import re
import yaml
from pprint import pprint
import os

def add_DBdata_to_dhcp(db_filename, dhcp_snoop_files):
	'''
	db_filename - имя БД
	dhcp_snoop_files - список файлов с выводом 
	
	Заполняет таблицу dhcp в БД
	'''
	db_exists = os.path.exists(db_filename)
	if not db_exists:
		print("Error! U need to create {} first!".format(db_filename))
		return
		
	db_exists = os.path.exists(db_filename)
	
	conn = sqlite3.connect(db_filename)
	
	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	result = []
	for sw_filename in dhcp_snoop_files:
		sw_name = re.match("([a-zA-Z\d]+)_dhcp",sw_filename)[1]
		with open(sw_filename) as f:
			for line in f:
				match = regex.search(line)
				if match:
					result.append( (match[1], match[2], match[3], match[4], sw_name) )
					
	for row in result:
		try:
			with conn:
				query = "insert into dhcp values (?,?,?,?,?)"
				conn.execute(query,row)
		except sqlite3.IntegrityError as e:
			print('Error, when writing: ', e)	
	
	conn.close()	
	return
	
	
def add_DBdata_to_switches(db_filename, yml_filename):
	'''
	db_filename - имя БД
	yml_filename - имя файла yml с данными о свичах 
	
	Заполняет таблицу switches в БД
	'''
	db_exists = os.path.exists(db_filename)
	if not db_exists:
		print("Error! U need to create {} first!".format(db_filename))
		return
		
	with open(yml_filename) as f:
		data = yaml.load(f)
	
	data = data['switches']
	conn = sqlite3.connect(db_filename)
	for sw, loc in data.items():
		values = (sw, loc)
		try:
			with conn:
				query = "insert into switches values (?,?)"
				conn.execute(query, values)
		except sqlite3.IntegrityError as e:
			print('Error occured: ', e)
			
	conn.close()	
	return





db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print(dhcp_snoop_files)


add_DBdata_to_switches(db_filename,'switches.yml')
add_DBdata_to_dhcp(db_filename, dhcp_snoop_files)




















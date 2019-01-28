#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 18.5a

Теперь в БД остается и старая информация.
И, если какой-то MAC-адрес не появлялся в новых записях, запись с ним,
может оставаться в БД очень долго.

И, хотя это может быть полезно, чтобы посмотреть, где MAC-адрес находился в последний раз,
постоянно хранить эту информацию не очень полезно.

Например, если запись в БД уже больше месяца, то её можно удалить.

Для того, чтобы сделать такой критерий, нужно ввести новое поле,
в которое будет записываться последнее время добавления записи.

Новое поле называется last_active и в нем должна находиться строка,
в формате: YYYY-MM-DD HH:MM:SS.

В этом задании необходимо:
* изменить, соответственно, таблицу dhcp и добавить новое поле.
 * таблицу можно поменять из cli sqlite, но файл dhcp_snooping_schema.sql тоже необходимо изменить
* изменить скрипт add_data.py, чтобы он добавлял к каждой записи время

Как получить строку со временем и датой, в указанном формате, показано в задании.
Раскомментируйте строку и посмотрите как она выглядит.

'''


from datetime import timedelta, datetime
'''
now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days=7)
print(now)
print(week_ago)
print(now > week_ago)
print(str(now) > str(week_ago))
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
	
	Заполняет таблицу dhcp в БД. 
	Если в таблице есть данные, помечает все записи как неактивные (поле active = 0),
	записываемые данные помечает как активные (active = 1)
	'''
	db_exists = os.path.exists(db_filename)
	if not db_exists:
		print("Error! U need to create {} first!".format(db_filename))
		return
		
	conn = sqlite3.connect(db_filename)
		
	now = str(datetime.today().replace(microsecond=0))
	
	regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
	result = []
	for sw_filename in dhcp_snoop_files:
		sw_name = re.match("([a-zA-Z\d]+)_dhcp",sw_filename)[1]
		with open(sw_filename) as f:
			for line in f:
				match = regex.search(line)
				if match:
					result.append( (match[1], match[2], match[3], match[4], sw_name, 1, now) )
	
	#удалить из БД все записи, которые были активны более Х дней назад
	old_date = str(datetime.today().replace(microsecond=0) - timedelta(days=7))
	with conn:
		query = "delete from dhcp where last_active <= '{}'".format(old_date)
		conn.execute(query)
	
		
	#обновить поле актив
	with conn:
		query = "update dhcp set active = 0"
		conn.execute(query)
	
	for row in result:
		try:
			with conn:
				query = "insert into dhcp values (?,?,?,?,?,?,?)"
				conn.execute(query,row)
		except sqlite3.IntegrityError:
			with conn:
				query = "update dhcp set active = 1 where mac = '{}'".format(row[0])
				conn.execute(query)
				query = "update dhcp set last_active = '{}' where mac = '{}'".format(row[6],row[0])
				conn.execute(query)
		
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




















#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает

Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob
import re
from pprint import pprint
import csv


sh_version_files = glob.glob('sh_vers*')
sh_version_files.sort()
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']


def parse_sh_version(output):
	output = output.split('\n')
	result = []
	
	for line in output:
		match = re.match("Cisco IOS Software.+Version (.+),"
						"|System image file is \"(.+)\""
						"|.+uptime is (.+)"	,line)
		if match:
			result.append(match[1] or match[2] or match[3])
	
	# Поменять местами эл списка, и преобраз в кортеж
	temp = result[1]
	result[1] = result[2]
	result[2] = temp
	#result = tuple(result)
	return result

def write_to_csv(file_to_write,data):
	with open(file_to_write,'w') as f:
		writer = csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
		writer.writerows(data)
		
	return
	
	

inventory_data = [headers]
for file_to_open in sh_version_files:
	with open(file_to_open) as f:
		sh_ver = f.read()
	sh_ver_list = parse_sh_version(sh_ver)
	sh_ver_list.insert(0, re.search('version_(.+)\.txt',file_to_open)[1])
	inventory_data.append(sh_ver_list)


#pprint(inventory_data)
write_to_csv('routers_inventory.csv',inventory_data)















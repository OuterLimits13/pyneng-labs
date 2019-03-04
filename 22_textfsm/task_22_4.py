#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 22.4

На основе примера textfsm_clitable.py из раздела TextFSM
сделать функцию parse_command_dynamic.

Параметры функции:
* словарь атрибутов, в котором находятся такие пары ключ: значение:
 * 'Command': команда
 * 'Vendor': вендор (обратите внимание, что файл index отличается от примера, который использовался в разделе, поэтому вам нужно подставить тут правильное значение)
* имя файла, где хранится соответствие между командами и шаблонами (строка)
 * значение по умолчанию аргумента - index
* каталог, где хранятся шаблоны и файл с соответствиями (строка)
 * значение по умолчанию аргумента - templates
* вывод команды (строка)

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - названия столбцов
* значения - соответствующие значения в столбцах

Проверить работу функции на примере вывода команды sh ip int br.

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
import clitable
import os

from pprint import pprint


def parse_command_dynamic(output, attributes, index_filename='index', templates_folder='templates'):
	if os.path.isfile(output):
		output = open(output).read()

	cli_table = clitable.CliTable(index_filename, templates_folder)
	cli_table.ParseCmd(output, attributes)

	result = []
	for row in cli_table:
		row = list(row)
		dict_row = dict(zip(cli_table.header, row))
		result.append(dict_row)
		
	return result



if __name__ == '__main__':
	attributes = {'Command': 'show ip int brief', 'Vendor': 'cisco_ios'}
	res = parse_command_dynamic('output/sh_ip_int_br.txt', attributes)
	pprint(res)













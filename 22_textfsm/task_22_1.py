#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 22.1

Переделать пример, который использовался в разделе TextFSM, в функцию.

Функция должна называться parse_output. Параметры функции:
* template - шаблон TextFSM (это должно быть имя файла, в котором находится шаблон)
* output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов (в примере ниже, находится в переменной header)
* остальные элементы это списки, в котором находятся результаты обработки вывода (в примере ниже, находится в переменной result)

Проверить работу функции на каком-то из примеров раздела.

Пример из раздела:
'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')

import textfsm
from tabulate import tabulate

def parse_output(template, output):
	result = []
	with open(template) as t, open(output) as output:
		re_table = textfsm.TextFSM(t)
		result.append(re_table.header)
		result.extend( re_table.ParseText(output.read()) )
		
	return result




if __name__ == "__main__":
	res = parse_output('templates/sh_ip_dhcp_snooping.template','output/sh_ip_dhcp_snooping.txt')
	print(res)
	print('= ' * 50)
	print(tabulate(res, headers='firstrow'))
	

	











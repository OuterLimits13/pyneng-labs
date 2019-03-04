#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 22.1a

Переделать функцию parse_output из задания 22.1 таким образом,
чтобы, вместо списка списков, она возвращала один список словарей:
* ключи - названия столбцов,
* значения, соответствующие значения в столбцах.

То есть, для каждой строки будет один словарь в списке.
'''


import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')

import textfsm
from tabulate import tabulate

def parse_output(template, output):
	result = []
	with open(template) as t, open(output) as output:
		re_table = textfsm.TextFoSM(t)
		for row in re_table.ParseText(output.read()):
			dict_row = dict(zip(re_table.header, row))
			result.append(dict_row)  
		
	return result




if __name__ == "__main__":
	res = parse_output('templates/sh_ip_int_br.template','output/sh_ip_int_br.txt')
	print(res)
	




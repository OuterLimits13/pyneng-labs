#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''

import re
from pprint import pprint

def parse_sh_ip_int_br(file_to_open):
	'''
	parse_sh_ip_int_br, которая ожидает как аргумент
	имя файла, в котором находится вывод команды show

	Возвращает список кортежей ( Interface , IP-Address , Status , Protocol)
	'''
	
	regex = '(\S+)\s+([0-9\.]+|unassigned)\s+\w+\s+\w+\s+(up|down|administratively down)\s+(up|down)' 
	result = []
	with open(file_to_open) as f:
		for line in f:
			mat = re.match(regex,line)
			if mat:
				result.append(mat.groups())
			
	return result






if __name__ == "__main__":
	res_list = parse_sh_ip_int_br('sh_ip_int_br_2.txt')
	pprint(res_list)








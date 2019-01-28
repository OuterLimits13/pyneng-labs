#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re
from pprint import pprint

def parse_cfg(file_to_open):	
	regex = ('interface (\S+)'
			'| ip address (\S+) (\S+)')
			
	result = {}
	with open(file_to_open) as f:
		for line in f:
			match = re.match(regex,line)
			
			if match and match[1] != None:
				intf = match[1]
				result[intf] = ()
			elif match and match[1] == None:
				result[intf] = match.group(2,3)
		
		
	return result






if __name__ == "__main__":
	res_list = parse_cfg('config_r1.txt')
	pprint(res_list)






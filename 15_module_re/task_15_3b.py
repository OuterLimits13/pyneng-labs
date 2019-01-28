#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''


import re
from pprint import pprint

def parse_cfg(file_to_open):	
				
	result = {}
	with open(file_to_open) as f:
		for line in f:
			match = re.match('interface (\S+)',line)
			if match:
				intf = match[1]
				result[intf] = []
				
			match = re.match(' ip address (\S+) (\S+)',line)
			if match:
				result[intf].append(match.group(1,2))
		
		
	return result






if __name__ == "__main__":
	res_list = parse_cfg('config_r2.txt')
	pprint(res_list)

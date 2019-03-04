#!/home/usr/new/pyneng/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 22.6

Это задание похоже на задание 22.5, но в этом задании подключения надо выполнять параллельно с помощью потоков.
Для параллельного подключения использовать модуль concurrent.futures.

В этом упражнении нужно создать функцию send_and_parse_command_parallel:
* она должна использовать внутри себя функцию send_and_parse_command
* какие аргументы должны быть у функции send_and_parse_command_parallel, нужно решить самостоятельно
* функция send_and_parse_command_parallel должна возвращать словарь, в котором:
 * ключ - IP устройства
 * значение - список словарей

Проверить работу функции send_and_parse_command_parallel на команде sh ip int br.

'''


from task_22_5 import send_and_parse_command
from concurrent.futures import ThreadPoolExecutor, as_completed
import yaml

from pprint import pprint



def send_and_parse_command_parallel(devices_list, command, function=send_and_parse_command, limit=4,
							attributes='Default', index_filename='index', templates_folder='templates'):
	
	all_results = {}
	with ThreadPoolExecutor(max_workers=limit) as executor:
		future_send_func = [ executor.submit (function, device,
							 command, attributes, index_filename, templates_folder) 
							 for device in devices_list ]
							 
		for f in as_completed(future_send_func):
			all_results.update(f.result())

	return all_results
	
	


if __name__ == '__main__':
	command = 'sh ip int bri | excl down'
	devices = yaml.load(open('devices.yaml'))
	
	res = send_and_parse_command_parallel(devices['routers'], command)
	pprint(res)


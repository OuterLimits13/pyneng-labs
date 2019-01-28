#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_commands_threads, которая запускает функцию send_commands из задания 19.3 на разных устройствах в параллельных потоках.

Параметры функции send_commands_threads надо определить самостоятельно.
Должна быть возможность передавать параметры show, config, filename функции send_commands.

Функция send_commands_threads возвращает словарь с результатами выполнения команд на устройствах:

* ключ - IP устройства
* значение - вывод с выполнением команд

'''

from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
sys.path.append('/home/usr/pyneng-labs/19_ssh_telnet/')
import yaml
from pprint import pprint
from task_19_3 import send_commands


def send_commands_threads(function, devices, limit=2, show=None, filename=None, config=None):
	all_results = {}
	if show:
		with ThreadPoolExecutor(max_workers=limit) as executor:
			future_send_func = [ executor.submit(function, device, show=show)
													   for device in devices ]
			for f in as_completed(future_send_func):
				all_results.update(f.result())
		return all_results
	if filename:
		with ThreadPoolExecutor(max_workers=limit) as executor:
			future_send_func = [ executor.submit(function, device, filename=filename)
													   for device in devices ]
			for f in as_completed(future_send_func):
				all_results.update(f.result())
		return all_results
	if config:
		with ThreadPoolExecutor(max_workers=limit) as executor:
			future_send_func = [ executor.submit(function, device, config=config)
													   for device in devices ]
			for f in as_completed(future_send_func):
				all_results.update(f.result())
		return all_results
		




if __name__ == '__main__':
	commands = ['no alias exec bri sh ip int br',  'no alias exec brit sh ip int br | i Tunn']
	command = 'sh run | i ntp'

	with open('devices_1.yaml') as f:
		devices = yaml.load(f)

	res = send_commands_threads(send_commands, devices['routers'], config=commands)
	pprint(res)
	
	



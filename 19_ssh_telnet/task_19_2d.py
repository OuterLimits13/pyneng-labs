#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 19.2d

В этом задании надо создать функцию send_cfg_to_devices, которая выполняет команды на нескольких устройствах последовательно и при этом выполняет проверку на ошибки в командах.

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* config_commands - список команд, которые надо выполнить

Функция должна проверять результат на такие ошибки:
* Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка, функция должна выводить сообщение на стандартный поток вывода с информацией о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

После обнаружения ошибки, функция должна спросить пользователя надо ли выполнять эту команду на других устройствах.

Варианты ответа [y]/n:
* y - выполнять команду на оставшихся устройствах (значение по умолчанию)
* n - не выполнять команду на оставшихся устройствах

Функция send_cfg_to_devices должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - IP устройства
* значение - вложенный словарь:
  * ключ - команда
  * значение - вывод с выполнением команд

В файле задания заготовлены команды с ошибками и без:
'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
import yaml
from pprint import pprint
import netmiko
import re

def send_cf_to_devices(devices_list, config_commands, verbose=True):
	
	successful_commands_on_devs = {}
	unsuccessful_commands_on_devs = {}
	regex = re.compile('(Invalid input detected|Incomplete command|Ambiguous command)')
	for device in devices_list:
		unsuccessful_commands = {}
		successful_commands = {}
		try:
			with netmiko.ConnectHandler(**device) as ssh:
				for number, command in enumerate(config_commands):
					if not command:
						continue
					print('=== ' + command + ' ===')
					result = ssh.send_config_set(command)						
					match = regex.search(result)
					if match:
						print('При выполнении комманды {} на устройстве {}, '
							  'возникла ошибка: {}'.format(command, device['ip'], match[1]))
						unsuccessful_commands[command] = result
						while True:
							answer = input('Хотите ли выполнять команду с ошибкой на др. устройствах [y]/n: ')
							if answer == 'y' or answer == '' or answer == 'n':
								break
						if answer == 'n':
							config_commands[number] = None
													
					elif not match:
						successful_commands[command] = result
						if verbose:
							print('Команда {} на устройстве {} выполнена'.format(command, device['ip']))
				
					
		except (netmiko.ssh_exception.AuthenticationException, netmiko.ssh_exception.NetMikoTimeoutException) as e:
			print('Error occurred: ', e)
		
		successful_commands_on_devs[device['ip']] = successful_commands
		unsuccessful_commands_on_devs[device['ip']] = unsuccessful_commands
	
	return (successful_commands_on_devs, unsuccessful_commands_on_devs)
	



commands_with_errors = ['logging 0255.255.1', 'logging']
correct_commands = ['no alias exec bri sh ip int br',  'no alias exec brit sh ip int br | i Tunn']
commands = commands_with_errors + correct_commands

with open('devices_1.yaml') as f:
	devices = yaml.load(f)

res = send_cf_to_devices(devices['routers'], commands)
pprint(res)
	

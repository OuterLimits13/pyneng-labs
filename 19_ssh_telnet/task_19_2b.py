#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 19.2b

В этом задании необходимо переделать функцию send_config_commands из задания 19.2a или 19.2 и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

При этом, параметр verbose также должен работать, но теперь он отвечает за вывод
только тех команд, которые выполнились корректно.

Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"

В файле задания заготовлены команды с ошибками и без:
'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
import yaml
from pprint import pprint
import netmiko
import re

def send_config_commands(device, config_commands, verbose=True):
	
	successful_commands = {}
	unsuccessful_commands = {}
	regex = re.compile('(Invalid input detected|Incomplete command|Ambiguous command)')
	try:
		with netmiko.ConnectHandler(**device) as ssh:
			for command in config_commands:
				result = ssh.send_config_set(command)						
				match = regex.search(result)
				if match:
					print('При выполнении комманды {} на устройстве {}, '
						  'возникла ошибка: {}'.format(command, device['ip'], match[1]))
					unsuccessful_commands[command] = result
				elif not match:
					successful_commands[command] = result
					if verbose:
						print('Команда {} на устройстве {} выполнена'.format(command, device['ip']))
				
	except (netmiko.ssh_exception.AuthenticationException, netmiko.ssh_exception.NetMikoTimeoutException) as e:
		print('Error occurred: ', e)
			
	
	return (successful_commands, unsuccessful_commands)
	



commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['no alias exec bri sh ip int br',  'no alias exec brit sh ip int br | i Tunn']
commands = commands_with_errors + correct_commands

with open('devices_1.yaml') as f:
	devices = yaml.load(f)

for device in devices['routers']:
	res = send_config_commands(device, commands)
	pprint(res)
	
	
	
	
	
	
	
	
	
	
	
	
	
	

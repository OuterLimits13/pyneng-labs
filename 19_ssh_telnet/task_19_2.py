#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 19.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет перечень команд в конфигурационном режиме на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
import yaml
from pprint import pprint
import netmiko

def send_config_commands(device, config_commands, verbose=True):
	command_result = {}
	
	try:
		with netmiko.ConnectHandler(**device) as ssh:
			result = ssh.send_config_set(config_commands)
			command_result[device['ip']] = result
			if verbose:
				print(command_result[device['ip']])
						
	except (netmiko.ssh_exception.AuthenticationException, netmiko.ssh_exception.NetMikoTimeoutException) as e:
		print('Error occurred: ', e)
	
	
	return command_result
	


if __name__ == '__main__':	
	commands = ['no al_ias exec bri sh ip int br',  'no alias exec brit sh ip int br | i Tunn']

	with open('devices_1.yaml') as f:
		devices = yaml.load(f)

	for device in devices['routers']:
		res = send_config_commands(device, commands)
	

















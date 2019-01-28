#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Отправить команду command на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_show_command.

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
import yaml
from pprint import pprint
import netmiko


def send_show_command(device, command):
	command_result = {}
	
	try:
		with netmiko.ConnectHandler(**device) as ssh:
			result = ssh.send_command(command)
			command_result[device['ip']] = result
	except (netmiko.ssh_exception.AuthenticationException, netmiko.ssh_exception.NetMikoTimeoutException) as e:
		print('Error occurred: ', e)
	
	
	return command_result


if __name__ == '__main__':
	command = 'sh ip int br | i Tunn'
	with open('devices.yaml') as f:
		devices = yaml.load(f)

	#pprint(devices)
	for device in devices['routers']:
		res = send_show_command(device, command)
		pprint(res)
	

























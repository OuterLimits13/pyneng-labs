#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к устройству, которому надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции, всегда будет передаваться только один из аргументов show, config, filename.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2
* filename - функция send_commands_from_file (ее надо написать по аналогии с предыдущими)

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и различных комбинация аргумента с командами:
    * списка команд commands
    * команды command
    * файла config.txt

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
import yaml
from pprint import pprint
import netmiko
from task_19_1 import send_show_command
from task_19_2 import send_config_commands

def send_commands(device, show=None, filename=None, config=None):
	if show:
		return send_show_command(device, show)
	if filename:
		return send_commands_from_file(device, filename)
	if config:
		return send_config_commands(device, config)
	
	
def send_commands_from_file(device, filename):
	command_result = {}
	try:
		with netmiko.ConnectHandler(**device) as ssh:
			result = ssh.send_config_from_file(filename)
			command_result[device['ip']] = result
							
	except (netmiko.ssh_exception.AuthenticationException, netmiko.ssh_exception.NetMikoTimeoutException) as e:
		print('Error occurred: ', e)
		
	return command_result
	
	
	

if __name__ == '__main__':
	commands = ['no alias exec bri sh ip int br',  'no alias exec brit sh ip int br | i Tunn']
	command = 'sh run | i ntp'

	with open('devices_1.yaml') as f:
		devices = yaml.load(f)

	for device in devices['routers']:
		res = send_commands(device, filename='config.txt')
		pprint(res)
















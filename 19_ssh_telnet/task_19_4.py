#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 19.4

Создать функцию send_commands_to_devices (для подключения по SSH используется netmiko).

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В этой функции должен использоваться список словарей, в котором не указаны имя пользователя, пароль, и пароль на enable (файл devices2.yaml).

Функция должна запрашивать имя пользователя, пароль и пароль на enable при старте.
Пароль не должен отображаться при наборе.

Функция send_commands_to_devices должна использовать функцию send_commands из задания 19.3.

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
import yaml
from pprint import pprint
import netmiko
import getpass
from task_19_3 import send_commands

def send_commands_to_devices(devices_list, show=None, filename=None, config=None):
	username = input('Введите логин для устройств: ')
	password = getpass.getpass(prompt='Введите пароль для устройств: ')
	
	for device_dict in devices_list:
		device_dict['username'] = username
		device_dict['password'] = password
	
	result = []
	for device in devices_list:
		result.append(send_commands(device, show, filename, config))
	
	return result
	
	

if __name__ == '__main__':
	commands = ['no alias exec bri sh ip int br',  'no alias exec brit sh ip int br | i Tunn']
	command = 'sh run | i ntp'

	with open('devices_1.yaml') as f:
		devices = yaml.load(f)

	res = send_commands_to_devices(devices['routers'], show=command)
	pprint(res)








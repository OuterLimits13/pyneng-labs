#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess

def check_ip_addresses(ip_list):
	'''
	Функция проверяет доступность IP-адресов.
	Вход: список IP-адресов.
	Выход: два списка: список доступных IP-адресов, список недоступных IP-адресов
	'''	
	available_ip, not_avail_ip = [],[]
	for ip in ip_list:
		print('Trying to ping {}'.format(ip))
		reply = subprocess.run('ping -c 2 -W 2 -n {}'.format(ip), shell=True, stdout=subprocess.PIPE, 
								stderr=subprocess.PIPE, encoding='utf-8')
		result_reply_str = reply.stdout.split('\n')[-3].split()
		if result_reply_str[0] == result_reply_str[3]:
			available_ip.append(ip)
		else:
			not_avail_ip.append(ip)
	
		
	return available_ip, not_avail_ip
	
	
	
if __name__ == "__main__":
	available_ip, not_avail_ip = check_ip_addresses(['10.172.32.177','10.172.32.179','10.172.32.251','10.172.33.252'])
	print(available_ip)
	print(not_avail_ip)

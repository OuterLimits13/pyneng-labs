#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

import subprocess


def check_ip_addresses(ip_list):
	'''
	Функция проверяет доступность IP-адресов.
	Вход: список IP-адресов или диапазон IP адресов
	Выход: два списка: список доступных IP-адресов, список недоступных IP-адресов
	'''	
	available_ip, not_avail_ip, = [],[]
		
	for item in ip_list:
		if '-' in item:
			ip_list.remove(item)
			ip_range_similar_part = item.split('.')
			
			last_octet_borders = ip_range_similar_part.pop(3).split('-')
			last_octet_borders[0] = int(last_octet_borders[0])
			last_octet_borders[1] = int(last_octet_borders[1])
			
			for k in range(last_octet_borders[0],last_octet_borders[1] + 1):
				ip_list.append('.'.join(ip_range_similar_part) + '.' + str(k))   
					
	
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
	available_ip, not_avail_ip = check_ip_addresses(['10.172.32.177','10.172.32.179-185'])
	print(available_ip)
	print(not_avail_ip)




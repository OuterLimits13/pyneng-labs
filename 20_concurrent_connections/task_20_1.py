#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 20.1

Переделать задание 19.4a таким образом, чтобы проверка доступности устройств
выполнялась не последовательно, а параллельно.

Для этого, можно взять за основу функцию check_ip_addresses из задания 12.1.
Функцию надо переделать таким образом, чтобы проверка IP-адресов выполнялась
параллельно в разных потоках.

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
from tabulate import tabulate
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor



def check_ip_address(ip_address):
	'''
	Функция проверяет доступность IP-адреса.
	Вход:  IP-адрес.
	Выход: True - если IP доступен
	'''	
	#print('Trying to ping {}'.format(ip))
	reply = subprocess.run('ping -c 3 -W 1 -n {}'.format(ip_address), shell=True, stdout=subprocess.PIPE, 
							stderr=subprocess.PIPE, encoding='utf-8')
	result_reply_str = reply.stdout.split('\n')[-3]
	match = re.search("([0-9]+) received",result_reply_str)
	
	result = True if match[1] != '0' else False
			
	return result
	
	
def threads_check_ip(function, list_ip, limit=2):
	with ThreadPoolExecutor(max_workers=limit) as executor:
		f_results = executor.map(function, list_ip)
	return list(f_results)
	
	
	
if __name__ == '__main__':
	list_ip = ['10.172.32.177','10.172.32.179','10.172.32.253','10.172.32.252','10.172.32.1',
			   '10.172.32.2', '10.172.32.155', '10.172.32.163', '10.172.32.166']
	results = threads_check_ip(check_ip_address, list_ip)
	availability_results = [x for x in zip(list_ip,results)]
	print(tabulate(availability_results,headers=('IP:','Available:') ))
	
	
	
	
	
	
	
	
	
	
	
	

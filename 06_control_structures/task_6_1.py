#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
# solution
while True:
	ip = input('Введите IP: ')
	ip = ip.split('.')
	try:
		ip = [int(address) for address in ip]
	except:
		print('Incorrect IPv4 address!')
		continue
	flag = False if len(ip) != 4 else True
	for address in ip:
		if not (0 <= address and address <= 255):
			flag = False

	if flag:
		break
	else:
		print('Incorrect IPv4 address!')


print('-'*20)
if 1 <= ip[0] and ip[0] <= 223:
	print('unicast')
elif 224 <= ip[0] and ip[0] <= 239:	
	print('milticast')
elif ip[0] == 0 and ip[1] == 0 and ip[2] == 0 and ip[3] == 0:
	print('unassigned')
elif ip[0] == 255 and ip[1] == 255 and ip[2] == 255 and ip[3] == 255:
	print('local broadcast')
else:
	print('unused')


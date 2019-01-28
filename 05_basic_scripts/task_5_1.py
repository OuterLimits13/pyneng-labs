#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
# solution
IP = input('Введите сеть (сеть/маска): ')
print('-' * 30)
IP = IP.split('/')

IP_oct = IP[0].split('.')                                                                            
IP_oct = [int(i) for i in IP_oct]  
print('Network: \n{:<10}{:<10}{:<10}{:<10}'.format(IP_oct[0],IP_oct[1],IP_oct[2],IP_oct[3]) )
print('{:08b}  {:08b}  {:08b}  {:08b}'.format(IP_oct[0],IP_oct[1],IP_oct[2],IP_oct[3]) )

prefix = int(IP[1])
prefix = '1' * prefix + '0' * (32 - prefix)
mask = []
mask.append(prefix[:8])
mask.append(prefix[8:16])
mask.append(prefix[16:24])
mask.append(prefix[24:])
mask = [int(m,2) for m in mask]
print('Mask: \n{:<10}{:<10}{:<10}{:<10}'.format(mask[0],mask[1],mask[2],mask[3]) )
print('{:08b}  {:08b}  {:08b}  {:08b}'.format(mask[0],mask[1],mask[2],mask[3]) )

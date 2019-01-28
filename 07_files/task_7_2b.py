#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
#solution
from sys import argv

config_commands = []

with open(argv[1]) as file_src:
	for line in file_src:
		matching = False
		for ignore_word in ignore:
			if line.count(ignore_word):
				matching = True
				break
			
		if matching:
			continue
		else:
			config_commands.append(line)
			
#print(config_commands)

with open('config_sw1_cleared.txt','w') as file_dest:
	file_dest.writelines(config_commands)






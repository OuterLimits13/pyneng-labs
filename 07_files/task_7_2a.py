#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

#solution
from sys import argv

config_commands = []
with open(argv[1]) as file:
	for line in file:
		if line.startswith('!'):
			continue
		else:
			config_commands.append(line.rstrip())
			
for command in config_commands:
	matching = False
	for ignore_word in ignore:
		if command.count(ignore_word):
			matching = True
			break
		
	if matching:
		continue
	else:
		print(command)

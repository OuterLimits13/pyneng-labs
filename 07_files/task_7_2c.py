#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

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
			
with open(argv[2],'w') as file_dest:
	file_dest.writelines(config_commands)



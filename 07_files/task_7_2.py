#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
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
	print(command)

#




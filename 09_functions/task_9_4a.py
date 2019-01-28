#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ignore = ['!','duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
	'''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
	'''
	return any(word in command for word in ignore)

def dict_config(config_file,ignore):
	'''
	Функця обрабатывает конфиг файл коммутатора. Игнорирует команды с словом из списка ignore.
	
	Возвращает словарь, где все команды глобального режима конфигурации -ключи, подкоманды - список значений
	'''
	
	with open(config_file) as file:
		file = file.read().strip().split('\n')
	
	dict_conf = {}
	for line in file:	
		if not ignore_command(line,ignore):
			if line[0] != ' ':
				global_conf_command = line
				dict_conf[global_conf_command] = []
			elif line[0] == ' ' and line[1] != ' ':
				level2_subcommand = line
				dict_conf[global_conf_command].append(level2_subcommand)
			else:
				# переделываем список в словаре, на словарь списков
				if type(dict_conf[global_conf_command]) != dict:
					dict_conf[global_conf_command] = dict.fromkeys(dict_conf[global_conf_command],[])
				dict_conf[global_conf_command][level2_subcommand].append(line)
			
	return dict_conf


result = dict_config('config_r1.txt',ignore)
for glob_key in result.keys():
	print(glob_key)
	print(result[glob_key])












#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 21.1

Переделать скрипт cfg_gen.py в функцию generate_cfg_from_template.

Функция ожидает два аргумента:
* путь к шаблону
* файл с переменными в формате YAML

Функция должна возвращать конфигурацию, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных data_files/for.yml.

'''

import sys
sys.path.append('/home/usr/new/pyneng/lib/python3.6/site-packages')
from jinja2 import Environment, FileSystemLoader
import yaml
import json
import os



def generate_cfg_from_template(path_to_template, data='', trim_blocks=True, lstrip_blocks=True):
	'''
	Функция создает конфигурацию из шаблона.
	Вход: 
		- path_to_template - Путь к файлу шаблона
		- data - файл в формате (.yml, .yaml, .json) или словарь, содержащие данные для шаблона
		- доп опции для Envorinment
	Выход: Выводит на станд поток вывода конфигурацию
	'''
	TEMPLATE_DIR, template = os.path.split(path_to_template)
	
	env = Environment(loader=FileSystemLoader(TEMPLATE_DIR),
				trim_blocks=trim_blocks, lstrip_blocks=lstrip_blocks)
	template = env.get_template(template)
	
	if type(data) == dict:
		vars_dict = data
	elif data.split('.')[-1] == 'yaml' or data.split('.')[-1] == 'yml':
		vars_dict = yaml.load(open(data))
	elif data.split('.')[-1] == 'json':
		vars_dict = json.load(open(data))
	else:
		print('Error! Поддерживаются файлы с расширением .json, .yml, .yaml и словари Python')
		return None
	
	print(template.render(vars_dict))
	
	return True



if __name__ == '__main__':

	data_dict = {
		'vlans': {
			10: 'Marketing',
			20: 'Voice',
			30: 'Management'},
		'ospf': [{'network': '10.0.1.0 0.0.0.255','area': 0}, 
				{'network': '10.0.2.0 0.0.0.255','area': 2}, 
				{'network': '10.1.1.0 0.0.0.255','area': 0}],
		'id': 3,
		'name': 'R3'}

	print(generate_cfg_from_template('templates/for.txt', 'data_files/for.yml'))



















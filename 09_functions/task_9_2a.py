#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию скрипта задания 9.2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


def generate_trunk_config(trunk):
	'''
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''
	trunk_template = [
        'switchport trunk encapsulation dot1q', 'switchport mode trunk',
        'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
	]
	
	result = {}
	for intf,allowed_vlans in trunk.items():
		intf = 'interface {}'.format(intf)
		result[intf] = []
		for command in trunk_template:
			if command.endswith('allowed vlan'):
				result[intf].append(' {} {}'.format(command, ','.join([str(vlan) for vlan in allowed_vlans]) ) )
			else:
				result[intf].append(' {}'.format(command))
	
									
	print('\nDone!\n')
	return result
	



trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


configure_trunk_ifs = generate_trunk_config(trunk_dict)

for intf, command_list in configure_trunk_ifs.items():
	print(intf)
	for command in command_list:
		print(command)
		
		
		
		
		
		
		
		
		
		

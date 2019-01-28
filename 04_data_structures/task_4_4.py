# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'


# решение
vlans=set(command1[command1.find('1'):].split(',') ) & set(command2[command2.find('1'):].split(',')) 
vlans=[int(i) for i in vlans]                                                                      
vlans.sort()  

# Или др решение
commands_1 = command1.split()
commands_2 = command2.split()
	# commands_2 = ['switchport', 'trunk', 'allowed', 'vlan', '1,3,100,200,300']

vlans=set(commands_1[-1].split(',')) & set(commands_2[-1].split(',')) 
vlans=[int(i) for i in vlans]                                                                      
vlans.sort()  

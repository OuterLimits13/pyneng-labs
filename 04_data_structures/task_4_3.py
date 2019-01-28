# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'


#
CONFIG_res=CONFIG[CONFIG.find('1')::].split(',')                                                

# or
CONFIG_res2=CONFIG.split()
CONFIG_res2=CONFIG_res2[-1].split(',')

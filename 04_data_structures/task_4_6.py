# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

# Решение
ospf_route_res=ospf_route.split()
ospf_route_res[2]=ospf_route_res[2].strip('[]')

# ospf_route_res = ['O', '10.0.24.0/24', '[110/41]', 'via', '10.0.13.3,', '3d18h,', 'FastEthernet0/0']

message_res=( 
'{protocol:<22} {ospf}\n' 
'{prefix:<22} {subnet}\n' 
'{ad_metric:<22} {route_ad_metric}\n' 
'{next_hop:<22} {nhop}\n' 
'{last_update:<22} {last_upd}\n' 
'{outbound_interface:<22} {outbound_if}\n')  

print( message_res.format(protocol='Protocol:',ospf='OSPF',
prefix='Prefix:',subnet=ospf_route_res[1],
ad_metric='AD/Metric:',route_ad_metric=ospf_route_res[2],
next_hop='Next-Hop:',nhop=ospf_route_res[4],
last_update='Last update:',last_upd=ospf_route_res[5],
outbound_interface='Outbound Interface:',outbound_if=ospf_route_res[6]) )







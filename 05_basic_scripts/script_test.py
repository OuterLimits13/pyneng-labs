#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# from sys import argv
# interface, vlan = argv[1:]

interface = input('Enter interface: ')
vlan = input('Enter vlan: ')


access_template=[' switchport mode access', ' switchport access vlan {}',' switchport nonegotiate',' spanning-tree portfast',' spanning-tree bpdufilter enable']

print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))

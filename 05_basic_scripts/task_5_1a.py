#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
'''

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
'''

# solution
IP = input('Введите подсеть или IP хоста (формата IP/mask): ')
print('-' * 30)
IP = IP.split('/')
IP_oct = IP[0].split('.')                     

IP_oct = [int(i) for i in IP_oct]  

prefix = int(IP[1])
prefix = '1' * prefix + '0' * (32 - prefix)
mask = []
mask.append(prefix[:8])
mask.append(prefix[8:16])
mask.append(prefix[16:24])
mask.append(prefix[24:])                                                       

IP_oct = [ '{:08b}'.format(IP_oct[i]) for i in range(4) ]
IP_oct = [ IP_oct[i][:mask[i].count('1')]  + '0' * (8 - mask[i].count('1')) for i in range(4) ]

print('Network: \n{:<10}{:<10}{:<10}{:<10}'.format(int(IP_oct[0],2),int(IP_oct[1],2),int(IP_oct[2],2),int(IP_oct[3],2) ) )
print('{:8}  {:8}  {:8}  {:8}\n'.format(IP_oct[0],IP_oct[1],IP_oct[2],IP_oct[3]) )

mask = [int(m,2) for m in mask]
print('Mask: \n{:<10}{:<10}{:<10}{:<10}'.format(mask[0],mask[1],mask[2],mask[3]) )
print('{:08b}  {:08b}  {:08b}  {:08b}'.format(mask[0],mask[1],mask[2],mask[3]) )




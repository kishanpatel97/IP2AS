#! /usr/bin/env python
# Kishan Patel 914983103

import sys
import os
infile = sys.argv[-1]
datafile = sys.argv[-2]
infile = open(os.getcwd() + '/' + infile, mode='r')
inIp = infile.read().splitlines()
infile.close()
datafile = open(os.getcwd() + '/' + datafile, mode='r')
data = datafile.read().splitlines()
datafile.close()
write = open('output.txt', 'w+')
for ip in inIp:
    ip_i = ip.split('.')
    ispIp = ''
    length = 0
    asn = ''
    for d in data:
        d = d.split(' ')
        ip_d = d[0].split('.')
        if ip_i[:2] != ip_d[:2]:
            continue
        try:
            b1 = ''.join([bin(int(i)+256)[3:] for i in ip_i])
            b2 = ''.join([bin(int(i)+256)[3:] for i in ip_d])
        except:
            continue
        l = int(d[1])
        if b1[:l] == b2[:l] and l >= length:
            ispIp = d[0]
            length = l
            asn = d[2]
    write.write(ispIp + '/' + str(length) + ' ' + asn + ' ' + ip+ '\n')
write.close()
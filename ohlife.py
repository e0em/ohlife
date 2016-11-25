#!/usr/bin/python27
# -*- coding: UTF-8 -*-
import sys
import codecs
remark = '趙永華 Marty Chao\r\nCISSP®/BS7799 LA/RHCE\n產品管理部 產品經理\n普羅通信股份有限公司\nTEL:886-3-6006899 Ext. 4830\nFAX:886-3-5972970\n303新竹縣湖口鄉湖口工業區中華路15-1號\nFreePP:24029757\nMSN: marty_chao@msn.com Skype:marty_chao\n'.split('\n')
print remark

file = codecs.open('/home/marty/ohlife/ohlife_20140921.txt','r',encoding='utf8')
for line in file:
    if line[0:1] == '20':
        pass
#        print line
#    elif line[0:1] != '20':
#        print line,
    elif line[0:4] == remark[0][0:4]:
        print 'OK' + remark[0]
print remark[0]
file.close()


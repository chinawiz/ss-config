#!/usr/bin/env python
# coding=utf-8
#
# Generate a list of dnsmasq rules with ipset for gfwlist
# Ref https://github.com/gfwlist/gfwlist

import datetime
import shutil

mydnsip = '127.0.0.1'
mydnsport = '5353'
ipsetname = 'gfwlist'
# Extra Domain;
EX_DOMAIN = [
    'google.com',
    'google.com.hk',
    'google.com.tw',
    'google.com.sg',
    'google.co.jp',
    'google.co.kr',
    'blogspot.com',
    'blogspot.sg',
    'blogspot.hk',
    'blogspot.jp',
    'blogspot.kr',
    'gvt1.com',
    'gvt2.com',
    'gvt3.com',
    '1e100.net',
    'blogspot.tw',
    'youtube.com'
]

tmpfile = '/tmp/gfwlisttmp'
# do not write to router internal flash directly
outfile = '/tmp/dnsmasq_list.conf'
rulesfile = './gfw_lite_list.conf'

fs = file(outfile, 'w')
fs.write('# gfw list ipset rules for dnsmasq\n')
fs.write('# updated on ' +
         datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
fs.write('#\n')

for each in EX_DOMAIN:
    fs.write('address=/%s/%s\n' %(each, mydnsip))

print 'write extra domain done'

fs.close()
print 'moving generated file to dnsmasq directory'
shutil.move(outfile, rulesfile)

print 'done!'

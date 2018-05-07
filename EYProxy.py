# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:07:14 2018

@author: Maddox.Meng

EY inner proxy
"""

url = 'https://cn.nytimes.com/'
host = 'amweb.ey.net'
proxyServers = ['amweb.ey.net',
                'CNWEB.ey.net']

def genProxy(url, host='amweb.ey.net', protocol='https', port='8443'):
    if 'https' not in url:
        protocol = 'http'
        port = '8080'
        #host = host + ':' + port
    proxy = {protocol:host+':'+port}
    return proxy


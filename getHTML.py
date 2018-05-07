# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:16:11 2018

@author: Maddox.Meng
"""

import requests
def getHTMLText(url, proxy={'https': 'amweb.ey.net:8443'}):
    try:
        r = requests.get(url, proxies=proxy, timeout = 10)
        r.raise_for_status()
        return r.text
    except:
        return "error"
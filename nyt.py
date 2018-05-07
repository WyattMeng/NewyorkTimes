# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:16:15 2018

@author: Maddox.Meng
"""

class Article(object):

#    def __init__(self, title, date, writer, summary, text, id, relateId):
    def __init__(self, title, date):
        self.title = title
        self.date = date
#        self.writer = writer
#        self.summary = summary
#        self.text = text
#        self.id = id
#        self.relateId = relateId

    def print_article(self):
        print(self.title, self.date)
        
ar = Article('HoustonRockets win NBA Championship 2018','2018/05/30')
#print_article(ar)
ar.print_article()

from bs4 import BeautifulSoup
from EYProxy import genProxy
from getHTML import getHTMLText

url = 'https://cn.nytimes.com/'
proxy = genProxy(url)
html = getHTMLText(url, proxy)
soup = BeautifulSoup(html, 'html.parser')

#h3 -- a,href,title
#subHeadline
#regularSummaryHeadline
#referListHeadline
#headline
#sfheadline

tagclass = ['subHeadline','regularSummaryHeadline','sfheadline','headline','commentSummaryHeadline']

acl={}
i=0
for h in soup.find_all('h3', class_=[c for c in tagclass]):
    if '招聘启事' not in h.find('a').text:
        #print (h)
        print (h.get('class'))
        print (h.find('a').get('title'))
        print (url+h.find('a').get('href'))
        
        title = h.find('a').get('title')
        href = url.rstrip('/')+h.find('a').get('href')
        
        acl[i] = {'title':title, 'href':href}
        i+=1

import requests
for k in acl:
    print (k, acl[k]['title'])
    aclurl = acl[k]['href']+'dual'
    urlPush = 'http://fivefilters.org/kindle-it/send.php?context=send&url='+aclurl
    data = {'email':'mmmkkf_22','domain': 2,'save':'yes'}
    proxy = genProxy(aclurl)
    response = requests.post(aclurl, data, proxies=proxy)


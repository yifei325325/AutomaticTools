#!/usr/bin/python
#coding:utf8
'''
Created on 2015年3月24日

@author: kenny

little web spider
'''
import urllib
import webbrowser as web

url = 'http://www.163.com'

content = urllib.urlopen(url).read()

#print content

f1 = open('e:/163.com.html','w')#打开本地e:\163.com.html，没有则创建一个该文件
f1.write(content)
web.open_new_tab('e:/163.com.html')
print 'complete'
#!/usr/bin/python
#coding:utf8
'''
Created on 2015年3月24日

@author: Administrator
'''
s = u'中文'
s1=s.encode('utf-8')
print s
def fun(a):
    return a
b = fun('hello')

print type(b)
print b
#!/usr/bin/python
#coding:utf8
'''
Created on 2015年3月24日

@author: kenny
'''
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md

device = mr.waitForConnection()
mr.sleep(1)
device.press('KEYCODE_POWER','DOWN_AND_UP')
mr.sleep(1)
device.press('KEYCODE_HOME','DOWN_AND_UP')
mr.sleep(1)

#解锁
lock_x = 537
lock_y1 = 1500
lock_y2 = 800
device.drag((lock_x,lock_y1),(lock_x,lock_y2))
#安装测试包
device.removePackage('com.ibaby')
mr.sleep(2)
'''
#启动程序
device.startActivity(component="com.ibaby/com.ibaby.Ui.Login.LoginMainActivity")
mr.sleep(2)
result = device.takeSnapshot()
result.writeToFile('d:\demo\snapshot\insatlled.png','png')
'''
print 'removed'
#mr.alert(u'如果已经看到监控画面，请点击确定按钮，测试将继续进行。否则，请等待。。。',u'温馨提示',u'确定')

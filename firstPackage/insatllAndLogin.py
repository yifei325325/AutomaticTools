#!/usr/bin/python
#coding:utf8
'''
Created on 2015年3月24日

@author: kenny
'''

print 'started'
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
import time
print 'import complete'
realtime = time.strftime('%m%d%H%M%S',time.localtime())
def unlock():#解锁
    lock_x = 537
    lock_y1 = 1500
    lock_y2 = 800
    device.drag((lock_x,lock_y1),(lock_x,lock_y2))
def install():#安装测试包
    device.installPackage('d:\demo\package\IBaby Care_20150311_v2.3.21_www.apk')
    mr.sleep(10)
    #启动程序
    device.startActivity(component="com.ibaby/com.ibaby.Ui.Login.LoginMainActivity")
    mr.sleep(2)
    result = device.takeSnapshot()
    result.writeToFile('d:\demo\snapshot\installed%s.png'%realtime,'png')
    print 'installed'
    
    #登录
    device.touch(537,1540,'DOWN_AND_UP')
    mr.sleep(1)
    result = device.takeSnapshot()
    result.writeToFile('d:\demo\snapshot\login%s.png'%realtime,'png')
    print 'login'
def remove():
    device.removePackage('com.ibaby')
    mr.sleep(1)
    #return 1
    
def listen():
    device.startActivity(component="com.ibaby/com.ibaby.Ui.Login.LoginMainActivity")
    mr.sleep(5)
    mr.alert(u'如果已经看到监控画面，请点击确定按钮，测试将继续进行。否则，请等待。。。',u'温馨提示',u'确定')
    listen_x = 135
    listen_y = 1795
    for i in range(1,5):
        device.touch(listen_x,listen_y,'DOWN_AND_UP')#listen
        print 'Listening...'
        mr.sleep(2)
        result1 = device.takeSnapshot()
        result1.writeToFile('d:\demo\ibaby\snapshot\listening %d.png'%i,'png')
        mr.sleep(8)
        device.touch(listen_x,listen_y,'DOWN_AND_UP')#close
        print 'closeing...'
        mr.sleep(2)
        result2 = device.takeSnapshot()
        result2.writeToFile('d:\demo\ibaby\snapshot\listenClose %d.png'%i,'png')
        mr.sleep(2)        
        print 'Total test',i,'times' 
    return 1   
    
def speak():
    if listened == 1:
        pass
    else:
        device.startActivity(component="com.ibaby/com.ibaby.Ui.Login.LoginMainActivity")
        mr.sleep(5)
        mr.alert(u'如果已经看到监控画面，请点击确定按钮，测试将继续进行。否则，请等待。。。',u'温馨提示',u'确定')
    speak_x = 408
    speak_y = 1795
    for i in range(1,5):
        device.touch(speak_x,speak_y,'DOWN_AND_UP')#listen
        print 'Speaking...'
        mr.sleep(2)
        result1 = device.takeSnapshot()
        result1.writeToFile('d:\demo\ibaby\snapshot\speaking %d.png'%i,'png')
        mr.sleep(8)
        device.touch(speak_x,speak_y,'DOWN_AND_UP')#close
        print 'Speak Closeing...'
        mr.sleep(2)
        result2 = device.takeSnapshot()
        result2.writeToFile('d:\demo\ibaby\snapshot\speakingClose %d.png'%i,'png')
        mr.sleep(2)        
        print 'Total test',i,'times'  


if __name__ == '__main__':
    device = mr.waitForConnection()
    mr.sleep(1)
    device.press('KEYCODE_POWER','DOWN_AND_UP')
    mr.sleep(1)
    device.press('KEYCODE_HOME','DOWN_AND_UP')
    mr.sleep(1)
    unlock()
 
    a = True
    while a:
        myChoice = mr.choice('which action will you do?',['install package','remove package','listen','speak'],'Choice',)
        if myChoice == 0:
            install()
        elif myChoice == 1:
            remove()
        elif myChoice == 2:
            listened = listen()
        elif myChoice == 3:
            speak()        
        elif myChoice == -1:
            a = False
    print 'test complete'






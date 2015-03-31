#!/usr/bin/python
#coding:utf8
'''
Created on 2015年3月24日

@author: kenny

Calculator
'''
import wx
def display():
    displayArea.GetValue()
def zero(event):
    displayArea.SetValue('0')
def one(event):
    displayArea.SetValue('1')
def two(event):
    displayArea.SetValue('2')
def three(event):
    displayArea.SetValue('3')
def four(event):
    displayArea.SetValue('4')
def five(event):
    displayArea.SetValue('5')
def six(event):
    displayArea.SetValue('6')
def seven(event):
    displayArea.SetValue('7')
def eight(event):
    displayArea.SetValue('8')
def nine(event):
    displayArea.SetValue('9')





app = wx.App()
win = wx.Frame(None,title = u'计算器',size = (215,315),style = wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)
button0 = wx.Button(win,label = '0',pos = (10,245),size = (70,30))
button0.Bind(wx.EVT_BUTTON,zero)
button1 = wx.Button(win,label = '1',pos = (10,210),size = (30,30))
button1.Bind(wx.EVT_BUTTON,one)
button2 = wx.Button(win,label = '2',pos = (50,210),size = (30,30))
button2.Bind(wx.EVT_BUTTON,two)
button3 = wx.Button(win,label = '3',pos = (90,210),size = (30,30))
button3.Bind(wx.EVT_BUTTON,three)
button4 = wx.Button(win,label = '4',pos = (10,175),size = (30,30))
button4.Bind(wx.EVT_BUTTON,four)
button5 = wx.Button(win,label = '5',pos = (50,175),size = (30,30))
button5.Bind(wx.EVT_BUTTON,five)
button6 = wx.Button(win,label = '6',pos = (90,175),size = (30,30))
button6.Bind(wx.EVT_BUTTON,six)
button7 = wx.Button(win,label = '7',pos = (10,140),size = (30,30))
button7.Bind(wx.EVT_BUTTON,seven)
button8 = wx.Button(win,label = '8',pos = (50,140),size = (30,30))
button8.Bind(wx.EVT_BUTTON,eight)
button9 = wx.Button(win,label = '9',pos = (90,140),size = (30,30))
button9.Bind(wx.EVT_BUTTON,nine)
button_Point = wx.Button(win,label = '.',pos = (90,245),size = (30,30))
button_Plus = wx.Button(win,label = '+',pos = (130,245),size = (30,30))
button_Minus = wx.Button(win,label = '-',pos = (130,210),size = (30,30))
button_Mitl = wx.Button(win,label = '*',pos = (130,175),size = (30,30))
button_Div = wx.Button(win,label = '/',pos = (130,140),size = (30,30))
button_Equ = wx.Button(win,label = '=',pos = (170,210),size = (30,65))
button_Ce = wx.Button(win,label = 'CE',pos = (170,140),size = (30,65))
displayArea = wx.TextCtrl(win,pos = (10,80),size = (190,50))
win.Show()
app.MainLoop()
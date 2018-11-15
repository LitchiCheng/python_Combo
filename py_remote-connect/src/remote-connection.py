# coding=utf-8
import win32api
import win32gui
import win32con
import os
import time

t=os.system('start mstsc')
time.sleep(1)
zhujubing = win32gui.FindWindow(None, u'远程桌面连接')
print(zhujubing)
bianjikuang = win32gui.FindWindowEx(zhujubing, None, 'ComboBoxEx32', None)
win32gui.SendMessage(bianjikuang, win32con.WM_SETTEXT, None, '192.168.192.5')
win32api.keybd_event(0x09,0,0,0)      # Tab
win32api.keybd_event(0x09,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(0x09,0,0,0)      # Tab
win32api.keybd_event(0x09,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(0x4F,0,0,0)      # O
win32api.keybd_event(0x4F,0,win32con.KEYEVENTF_KEYUP,0)

time.sleep(1)
win32api.keybd_event(0x09,0,0,0)      # Tab
win32api.keybd_event(0x09,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(0x53,0,0,0)     #s
win32api.keybd_event(0x45,0,0,0)     #e
win32api.keybd_event(0x45,0,0,0)     #e
win32api.keybd_event(0x52,0,0,0)     #r
time.sleep(1)
lianjieanniu = win32gui.FindWindowEx(zhujubing, None, 'Button',u'连接(&N)')
win32gui.PostMessage(lianjieanniu, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
win32gui.PostMessage(lianjieanniu, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
time.sleep(0.8)
win32api.keybd_event(0x0D,0,0,0)    #回车
time.sleep(1)
win32api.keybd_event(0x59,0,0,0)    #Y



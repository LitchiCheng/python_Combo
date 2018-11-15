import win32api
import win32con
import time
import win32gui
#x, y = win32api.GetCursorPos()
#print(x, "  ", y)
#zhujubing = win32gui.FindWindow(None, u'yd3')
#win32gui.SetActiveWindow()
while(1):
    win32api.SetCursorPos((1119, 452))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 200, 0, 0)
    time.sleep(200)
    win32api.SetCursorPos((1121, 500))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 200, 0, 0)
    time.sleep(900)

import pyautogui as pag
screenWidth, screenHeight = pag.size()
#  返回一个Pillow/PIL的Image对象
img=pag.screenshot()
img.save('foo.png')
#pag.screenshot('foo.png')
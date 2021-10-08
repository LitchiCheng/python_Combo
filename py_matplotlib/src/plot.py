import matplotlib.pyplot as plt
import matplotlib.font_manager as fm        #字体管理器
import cv2
#my_font = fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")          #中文字体路径
x_data = ['2012', '2013']
y_data1 = [5699, 2323]          #param of plot should be list
y_data2 = [2323, 3232]
x1 = plt.plot(x_data, y_data1, color = 'pink', linewidth = 2.0, linestyle = '-.', label = 'shadiao')    #set format
x2 = plt.plot(x_data, y_data2, color = 'red', linewidth = 2.0, linestyle = '-', label = 'sdsfsd')
#plt.plot(x_data,y_data1,x_data,y_data2)
plt.legend(loc = 'best' )                   #set location
plt.xlabel("x")
plt.ylabel("y")     #set y name
plt.title('test')
ax = plt.gca()      #更细致的坐标轴修改
ax.xaxis.set_ticks_position('bottom') #设置刻度值的位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_color('red')          #设置轴线的颜色
ax.spines['bottom'].set_position(('data', 2300))       #设置轴线在哪个数值的位置
plt.subplot(2, 2, 1)            # the same as plt.subplot(222), 222是一个三位数，跟前面是一样的，把图标分成三块
import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(2, 3)
x1 = plt.subplot(gs[0, :])
x2 = plt.subplot(gs[1, 0])

plt.show()
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm        #字体管理器
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

plt.show()
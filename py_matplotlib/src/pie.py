import matplotlib.pyplot as plt
data = [1,23,443,52,2]
labels= ['a', 'b', 'c', 'd', 'e']
explode = [0, 0.3, 0, 0 ,0]
color = ['red', 'pink', 'yellow', 'blue', 'green']
plt.axes(aspect = 'equal')      #将横纵坐标轴标准化，正圆
plt.xlim(0, 8)
plt.ylim(0, 8)  #控制x轴y轴的范围
plt.pie(x= data,
        explode = explode, #突出显示
        labels = labels, #添加编程语言标签
        colors = color, #设置饼图的自定义填充色
        autopct= '%.3f%%',  #设置百分比的格式，此处保留3位小数
        pctdistance= 0.8,   #设置百分比标签与圆心的距离
        labeldistance= 1.15,    #设置标签与圆心的距离
        startangle= 180,    #设置饼图的初始角度
        center = (4, 4),    #设置饼图的圆心,相当于x轴和y轴的范围
        radius = 3.8,    #设置饼图的半径，相当于x轴和Y轴的范围
        counterclock= False,    #是否为逆时针，这里顺时针
        wedgeprops={'linewidth': 1, 'edgecolor' : 'green'}, #设置饼图内外边界的属性值
        textprops= {'fontsize': 12,'color':'black'},    #设置文本标签的属性
        frame= 1)   #是否显示饼图的圆圈
plt.title('pie')
plt.show()
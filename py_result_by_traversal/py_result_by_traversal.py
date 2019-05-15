bs1 = range(1,17)
bs2 = range(1,7)
caiyang = input("采样点：")
for i in bs1 :
    for j in bs2:
        rate = (i + 1) / (j + i + 1)
        if ((rate*100) == int(caiyang)):
            print("bs1: "+str(i)+" bs2: "+str(j))
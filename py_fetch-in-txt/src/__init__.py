import re
import sys,os
from os import path
import numpy as np
address = sys.argv[1]
address = sys.argv[1].replace('\\','\\\\')
pwd = os.getcwd()
pwd = pwd.replace('\\','\\\\')
out_address = pwd + '\\\\out-result.txt'
f1 = open(address,'r')
f2 = open(out_address,'w+')
count = 0
key_word = input("输入关键字： ")
for line in f1.readlines():
    if re.findall(key_word ,line):                  #查找“key_word”的行
        # f2.write(line)                              #把查找到的行写入f2.
        data_array = re.split("[|]", line)
        str_t = (data_array[3] + data_array[1])
        com = "0x" + str_t.split("0x")[1]+str_t.split("0x")[2]
        # print(np.int16(int(com,16)))
        new_data = data_array[0].replace("[0x183",("["+str(np.int16(int(com,16)))+"]\n"))
        f2.write(new_data)
        count = count + 1
    else:
        f2.write(line)
f1.close()
f2.close()
print("找到的行数：",count)
os.system("pause")
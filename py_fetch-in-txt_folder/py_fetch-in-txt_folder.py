import re
import sys,os
from os import path
address = sys.argv[1]
address = sys.argv[1].replace('\\','\\\\')
pwd = os.getcwd()
pwd = pwd.replace('\\','\\\\')
out_address = pwd + '\\\\out-result.txt'
#f1 = open(address,'r')
f2 = open(out_address,'w+')
filenames=os.listdir(address)
count = 0
key_word = input("输入关键字： ")
for filename in filenames:
    filepath = address+'/'+filename
    for line in open(filepath):
        if re.findall(key_word ,line):                  #查找“key_word”的行
            f2.write(line)                              #把查找到的行写入f2.
            count = count + 1;
# f1.close()
f2.close()
print("找到的行数：",count)
os.system("pause")
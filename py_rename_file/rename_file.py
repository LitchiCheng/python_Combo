#coding=utf-8 
import re
import sys,os
from os import path

def renameAllFile(suffix_old, suffix_new):
    address = sys.argv[1].replace('\\','\\\\')
    #获取目标文件夹的路径
    filedir = address
    #获取当前文件夹中的文件名称列表  
    filenames=os.listdir(filedir)
    #打开当前目录下的result.txt文件，如果没有则创建
    f=open('merge_result.txt','w')
    #先遍历文件名
    for filename in filenames:
        filepath = filedir+'/'+filename
        #遍历单个文件，读取行数
        rename = filepath.split(".")[0] + suffix_new
        os.rename(filepath, rename)

renameAllFile(".LRV",".mp4")
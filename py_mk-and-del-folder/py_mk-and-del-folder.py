import os
import shutil

def make_folder(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return True
    else:
        return False

def del_file(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        return True
    else:
        shutil.rmtree(path)
        return False

mkpath="\\folder_name\\"        #填你想命名的文件夹名
pwd = os.getcwd()
pwd = pwd.replace('\\','\\\\')
out_address = pwd + mkpath

del_file(out_address)         #先删掉

make_folder(out_address)        #创建当前目录下的文件夹
import os
import shutil
filter=[".cpp",".h",".c"] #设置过滤后的文件类型 当然可以设置多个类型

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

def all_path(dirname):

    result = []#所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        # print("1:",maindir) #当前主目录
        # print("2:",subdir) #当前主目录下的所有目录
        # print("3:",file_name_list)  #当前主目录下的所有文件

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容

            if ext in filter:
                result.append(apath)
    # print("数量是：" + str(len(file_name_list)))
            
    print("数量是：" + str(len(result)))
    return result

# print(all_path("D:\code\DIO-2000-CLEAN\SeerDIOBoard - 1.9.0 clean"))

#运行结果
#['E:\\myTest\\txt1.txt', 'E:\\myTest\\txt2.txt', 'E:\\myTest\\test1\\txt11.txt', 'E:\\myTest\\test2\\txt21.txt', 'E:\\myTest\\test2\\txt22.txt']



file_list = all_path("D:\code\DIO-2000-CLEAN\SeerDIOBoard - 1.9.0 clean")

mkpath="\\merge\\"        #填你想命名的文件夹名
pwd = os.getcwd()
pwd = pwd.replace('\\','\\\\')
out_address = pwd + mkpath

del_file(out_address)         #先删掉

make_folder(out_address)        #创建当前目录下的文件夹
 
for name in file_list:
    try: 
        shutil.copy(name, out_address)
    except Exception:
        pass

'''
所有的异常类都是从BaseException派生而来，用户要自定义异常，应该继承BaseException的子类Exception
'''
# try:
#     a = input("输入A \n")
#     b = input("输入B \n")
#     c = a / b
#     print("两数相除的结果是：", c)
# except IndexError:
#     print("索引错误")
# except ValueError:
#     print('数值错误')
# except ArithmeticError:
#     print('算术错误')
# except Exception:               #通常把该异常放在最后，因为所有异常都是该类的子类
#     print('未知错误')

'''
多异常捕获，省略异常类表示捕获所有异常
'''
# try:
#     a = input("sdf \n")
#     b = input("sdfs \n")
#     c = a / b
#     print(c)
# except (IndexError, ValueError, ArithmeticError):
#     print("sdfs")
# except:
#     print("wrong")

'''
访问异常信息
每个异常对象都有特定的属性和方法args, errno, strerror, with_traceback()
'''
def foo():
    try:
        fis = open("a.txt")
    except Exception as e:
        print(e.args)       #args包含了errno和strerror的元组
        print(e.errno)      #errno包含了错误编号
        print(e.strerror)     #strerror包含了错误描述字符串

# foo()

'''
else的使用
如果以往某段代码的异常能够被except捕获，那就放在try里面，如果希望向外传播，则放在else块里面。
'''
try:
    pass
except:
    pass
else:
    pass

'''
使用finally回收资源
1.程序在try块中打开了一些物理资源如端口，磁盘文件，网络连接等，这些物理资源必须显示的回收
2.不要在finally块中使用return或raise语句，会导致try和except中的return和raise语句失效
'''
try:
    #业务逻辑
    pass
except:
    pass
else:
    pass
finally:
    #回收资源
    pass

'''
使用raise引发异常
需要程序中自行引发异常，raise语句：
单独raise，引发异常，默认为依法RuntimeError异常
raise异常类
'''
# try:
#     x = input("fsdfs")
#     if x < 10:
#         raise           #不用try...except语句，直接raise，程序会中止退出
# except Exception:
#     print("shit")

'''
自定义异常类
'''
class LaJiException(Exception):pass         #简单即可，主要用命名



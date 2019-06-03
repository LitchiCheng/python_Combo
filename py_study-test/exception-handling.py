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

'''
函数和lambda表达式
'''
def returnTwoReturn():
    a = 12
    b = 13
    return a, b

# test_returnTwoReturn = returnTwoReturn()
# print(test_returnTwoReturn)
# test_a, test_b = returnTwoReturn()
# print(test_a)
# print(test_b)

'''
有一个数列，f(0) = 1, f(1) = 4, f(n+2) = 2*f(n+1) +f(n) ,其中n是大于0的整数， 求f(10)的指
'''
def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2*fn(n-1) + fn(n-2)

# print(fn(10))

def keywordParameterFuction(param1, param2):
    return param1, param2

# print(keywordParameterFuction(param1 = 1, param2 = 2))
# print(keywordParameterFuction(1,2))

'''
python 要求带默认参数的参数要放在形参列表的最后面
'''
def paramDefaultValue(param1 = 1, param2 = 2):
    return param1,param2

# print(paramDefaultValue())
# print(paramDefaultValue(1,1))

'''
参数收集（个数可变的参数）
'''
def mutableParameterNumber(param1, *mutable_param):
    for i in mutable_param:                 # mutable_param 这一系列的参数被看作是元组传入
        print(i)
    print(param1)

# mutableParameterNumber(12, 32,42,12,32)

'''
收集关键字参数
'''
def mutableKeywordParamNumber(param1, *mutable_param, **mutable_keyword_param):     # 关键字参数收集被看作是字典传入
    print(param1)
    for i in mutable_param:
        print(i)
    print(mutable_keyword_param)

# mutableKeywordParamNumber(11, 23,12, aa = 23, hh = 32)

'''
变量的作用域
'''
x = 5
def actionScopeOfVar():
    age = 20
    print(age)
    print(locals())
    print(locals()['age'])
    locals()['age'] = 12            # locals()对局部变量进行修改，但是不会影响局部变量，但是locals和globals对全局变量修改则有效
    print(age)
    globals()['x'] = 15     #对全局变量进行修改，则产生了影响
    print(x)
# print(locals())         #locals在全局范围，也是取得全局变量的“变量数组”
# actionScopeOfVar()

'''
全局变量默认可以在所有函数中被访问，但是如果函数中定义了和全局变量相同的变量名，那全局变量就被遮蔽，就是没有用。
'''
name = 'ssss'
sex = 'nan'
def globalVarInFunctionTheSame():
    # print(name)
    # name = 'sdfsf'            #这句局部变量就不能声明，因为前面还在用着name这个全局变量，后面就给它屏蔽了
    print(globals()['name'])        #使用访问全局变量的方式访问就不会有这样的问题
    name = 'werwe'
    global sex          #用global来声明全局变量
    print(sex)
    sex = 'nv'

# globalVarInFunctionTheSame()

'''
所有函数都是function对象，可以把函数本身赋值给变量。
'''
def functionIsObject(param1, param2):
    print(param1)
    print(param2)

print_two_param = functionIsObject
# print_two_param(1,2)

'''
lambda表达式必须使用关键字lambda，冒号左边是参数，冒号右边是表达式的返回值
'''
def returnAPlusB(a1,b1):
    a = a1
    b = b1
    return a+b

function = lambda a1,b1:a1 + b1     

# print(function(1,1) == returnAPlusB(1,1))
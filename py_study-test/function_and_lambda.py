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

mutableKeywordParamNumber(11, 23,12, aa = 23, hh = 32)

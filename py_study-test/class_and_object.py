'''
类所包含的最重要的两个成员就是方法和变量，其中类变量属于类本身，用于定义该类本身所包含的状态和数据，
实例变量则属于该类的对象，用于定义对象所包含的状态和数据，方法则用于定义该类的对象的行为或功能实现。
'''
class Person:
    hair = 'black'                      #类的变量
    def __init__(self, name = 'wangbadan', age = 8):            #构造方法，用于构造类的对象
        self.name = name            #实例变量
        self.age = age 
    def say(self, content):          #定义了一个方法
        print(content)
    
p = Person()
# print(p.name, p.age)
# p.name = 'gaoxiao'
# print(p.hair)
# p.say('sfdasdfa')
# w = Person()
# print(w.hair)

'''
python是动态语言，可以动态删除增加实例变量，也可以动态增加方法，不过有区别
'''
p.height = 12       #增加height变量
del p.name             #删除name变量，后面再访问就会出错,但是不会对其他对象造成影响，如下
w = Person()
# print(w.name)
# print(p.height)

'''
p对象动态增加方法，python不会自动将调用者自动绑定到第一个参数
'''
def addMethod(self, content):
    print('sdf',self, content)

p.add_method = addMethod            
p.add_method(p, "sdfdf")     #手动绑定到第一个参数, 否则会报缺形参,不像本身存在的方法，self不用传入参数


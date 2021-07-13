#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2020/10/19 10:45
# @Author : Cheng
# @File : python-class-b.py
# @Software : PyCharm

'''
Python中一切皆对象
●类与对象
    1、数据类型（不同的数据类型属于不同的类）
    2、对象（类之下包含的个例，称为实例或对象）

●类的组成（类属性、实例方法、静态方法、类方法）

●类的创建
class Student: # 类名由一个或多个单词组成，每个单词首字母大写，其余小写
     pass

●对象的组成:内存（id）、数据类型（type）、值
'''


'''
class Student:
    native_place = '安徽' # 直接写在类里的变量，成为类属性
      # 初始化方法
    def __init__(self,name,age):
        self.name = name    # self.name称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age = age

      # 实例方法
    def eat(self):          # 在类之外定义的称为函数，类之内定义的成为方法
        print('吃饭')

      # 静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod静态修饰，所以我是静态方法')

      # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

# 创建Student类的对象
stu1 = Student('张三',20)
stu1.eat() #对象名.方法名
# Student.eat(stu1) 类名.方法名(类的对象)-->实际上就是方法定义处的self
# 类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
# 类方法、静态方法，使用类名直接访问
print(Student.native_place)
Student.method()
Student.cm()

stu1.gender = '男'        # 动态绑定属性
def show():
    print('我是函数')
stu1.show = show()        # 动态绑定方法
'''


'''
●面向对象的三大特征
    ●封装:提高程序的安全性
        ●将数据(属性)_和行为(方法)包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复杂度。
        ●在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个'_'。
    ●继承:提高代码的复用性
    ●多态:提高程序的可扩展性和可维护性

# 封装
class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def show(self):
        print(self.name,self.__age)

stu = Student('张三',20)
print(dir(stu))
print(stu._Student__age) #在类的外部可以通过 _Student__age访问（君子协定，完全靠自觉）
'''

'''
# 继承(可以多继承)
class Person(object):            #Person继承Object类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_num):
        super(Student,self).__init__(name,age)
        self.stu_num = stu_num

    def show(self):               #方法重写
        super(Student, self).show()
        print(self.stu_num)

stu = Student('张三',20,'1001')
stu.show()
'''

'''
●object类
    ●object类是所有类的父类，因此所有类都有object类的属性和方法。
    ●内置函数dir()可以查看指定对象所有属性
    ●Object有一个__str__()方法，用于返回一个对于“对象的描述”,对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对__str__()进行重写

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '我的名字是{0},今年{1}岁'.format(self.name,self.age)

stu = Student('张三',20)
print(stu)           #默认调用__str__()这样的方法,原先是返回对象存放的内存地址(16进制)
'''

'''
# 多态
●简单地说，多态就是“具有多种形态”，它指的是:即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法。
●静态语言和动态语言关于多态的区别
    ●静态语言实现多态的三个必要条件
        ●继承
        ●方法重写
        ●父类引用指向子类对象
    ●动态语言的多态崇尚“鸭子类型”当看到一只鸟走起来像鸭子、游泳起来像鸭子、收起来也像鸭子，那么这只鸟就可以被称为鸭子。在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为。
'''


'''
# 特殊属性
# __dict__ 获得类对象或实例对象所绑定的所有属性和方法的字典
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
class D:
    pass

x = C('Jack',20)
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)  # 类对象的属性、方法字典
print(x.__class__)  # <class '__main__.C'>输出流对象所属的类
print(C.__bases__)  # 类的父亲元素的元组
print(C.__base__)  # 类的基类(最靠近C的父亲类)
print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # 子类的列表
'''

# 特殊方法
# __len__()
# __add__()
# __new__() 用于创建对象
# __init__() 对创建的对象进行初始化
'''
class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)         # len()是内置函数
stu1 = Student('张三')
stu2 = Student('Jack')
print(stu1.__add__(stu2))          # 与stu1 + stu2一样，在Student类中编写了__add__()方法
print(stu1.__len__())              # 与len(stu1)一样
'''

'''
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为:{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建对象的id为:{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为:{0}'.format(id(self)))
        self.name = name
        self.age = age

print('object这个类对象的id:{0}'.format(id(object)))
print('Person这个类对象的id:{0}'.format(id(Person)))
p1 = Person('张三',20)
print('p1这个Person类的实例对象的id:{0}'.format(id(p1)))
'''

'''
类的浅拷贝和深拷贝
    ●变量的赋值操作
        ●只是形成两个变量，实际上还是指向同一个对象
    ●浅拷贝
        ●Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝,
    因此，源对象与拷贝对象会引用同一个子对象
    ●深拷贝
        ●使用copy模块的deepcopy函数， 递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk
cpu1 = CPU()
disk1 = Disk()
computer1 = Computer(cpu1,disk1)

import copy
#浅拷贝
computer2 = copy.copy(computer1)
#深拷贝
computer3 = copy.deepcopy(computer1)
'''

'''
●模块
    ●模块英文为Modules
    ●函数与模块的关系
        ●一个模块中可以包含N多个函数
    ●在Python中一个扩展名为.py的文件就是一个模块
    ●使用模块的好处
        ●方便其它程序和脚本的导入并使用
        ●避免函数名和变量名冲突
        ●提高代码的可维护性
        ●提高代码的可重用性

●包
    ●包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录
    ●作用:
        ●代码规范
        ●避免模块名称冲突
    ●包与目录的区别
        ●包含_ init_ .py文件的目录称为包
        ●目录里通常不包含__init__.py文件
    ●包的导入
        import 包名
        import 模块名
        import 包名.模块名
        from 包名 import 模块名
        ...
'''


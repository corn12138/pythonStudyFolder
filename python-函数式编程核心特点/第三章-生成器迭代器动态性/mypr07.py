# 动态语言特性_动态给类添加静态方法和类方法

class Person():
    pass


# 动态添加静态方法---静态方法是类对象的方法，需要用装饰器@staticmethod来标识其为静态方法
@staticmethod
def staticFunc():
    print('--static Method--')

Person.staticFunc = staticFunc
Person.staticFunc()
Person.score =1000 # 动态添加属性
print(Person.score)

# 动态添加类方法---类方法是类对象的方法，需要用装饰器@classmethod来标识其为类方法
@classmethod
def clsFunc(cls):
    print('--class Method--')

Person.clsFunc = clsFunc
Person.clsFunc()

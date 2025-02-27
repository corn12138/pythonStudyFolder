# 动态语言特性_动态给对象添加属性和方法
import types


class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age



p1 = Person("zhangsan", 18)
p2 = Person("lisi", 20)

# 动态添加属性和方法
p1.score = 100
print(p1.score)

def run(self):
    print(f"{self.name} is runnin....")

p1.run = types.MethodType(run, p1)
p1.run()
p2.run() # AttributeError: 'Person' object has no attribute 'run'


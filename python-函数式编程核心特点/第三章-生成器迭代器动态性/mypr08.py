#动态语言特性_slots限制成员属性和方法
 # _slots_限制成员属性和方法:对动态添加成员变量、成员方法有限制，对动态添加类属性、类方法没有限制
 # _slots_ 只对本类有限制，对子类不起作用

class Person:
    __slots__ = ("name", "age", "score") # 限制成员属性和方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 100
    def eat(self):
        print("eat....")

if __name__ == '__main__':
    p1 = Person("zhangsan", 18)
    p1.gender = "man" # AttributeError: 'Person' object has no attribute--限制成员属性和方法,不能动态添加成员属性
    print(p1.name)
    print(p1.age)
    print(p1.score)
    p1.eat()
    p1.score = 200
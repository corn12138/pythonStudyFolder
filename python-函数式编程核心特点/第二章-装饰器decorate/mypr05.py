# 回顾内置装饰器(propery、staticmethod、classmethod)

# 1. property --- 用于将方法变成属性
class User:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    @property
    def year_salary(self):
        return int(self.__salary) * 12

if __name__ == '__main__':
    u1 = User("zhangsan", 30000)
    print(u1.year_salary) # 360000

# 2. staticmethod ---  它的作用是可以访问类变量
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def say_hello():
        print("hello")

if __name__ == '__main__':
    p1 = Person("zhangsan", 20)
    p1.say_hello() # hello


# 3. classmethod --- 用于访问类变量
class Person:
    country = "中国"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def get_country(cls):
        return cls.country

if __name__ == '__main__':
    p1 = Person("zhangsan", 20)
    print(p1.get_country()) # 中国
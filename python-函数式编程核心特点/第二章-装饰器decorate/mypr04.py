# wraps装饰器
# 作用：保留原函数的元信息,如函数名、文档字符串、注解等

from functools import wraps

def mylog(func):
    @wraps(func)
    def inner(*args, **kwargs):

        print("日志记录....")
        print("函数文档：", func.__doc__)
        return func(*args, **kwargs)
    return inner

@mylog
def fun1():
    """
    这是功能1
    """
    print("使用功能1")

if __name__ == '__main__':
    fun1()
    print("函数文档-----》",fun1.__doc__)
    print(fun1.__name__) # fun1
    print(fun1.__module__) # __main__
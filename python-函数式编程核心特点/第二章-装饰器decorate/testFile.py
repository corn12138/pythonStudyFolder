

import time
from functools import wraps

# 缓存装饰器
class CacheDecorator:
    __cache = {} # 这是整个类的静态变量，用来存储缓存的数据
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        """缓存装饰器"""
        #如果缓存中有对应的方法名，则直接返回缓存中的值
        if self.func.__name__ in CacheDecorator.__cache:
            return CacheDecorator.__cache[self.func.__name__]
        #如果缓存中没有对应的方法名，则调用原方法，并将结果存入缓存
        else:
            result = self.func(*args, **kwargs)
            CacheDecorator.__cache[self.func.__name__] = result
            return result


class TestTime:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        start = time.time()
        result= self.func(*args, **kwargs)
        end = time.time()
        print(f"耗费的时间:{ end - start}")
        return result

@TestTime
@CacheDecorator
def myfunc(*args, **kwargs):
    print("start func1")
    time.sleep(3)
    print("end func1")
    return 999

if __name__ == '__main__':
    r1 = myfunc()
    r2 = myfunc()
    print(r1, r2)
    # print("函数名：", myfunc.__name__)
    # print("函数文档：", myfunc.__doc__)
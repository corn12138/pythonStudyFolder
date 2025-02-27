# 缓存和计时装饰器的综合练习

import time

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
            result = self.func(*args, **kwargs) #调用原方法
            CacheDecorator.__cache[self.func.__name__] = result #将结果存入缓存
            return result #返回结果


class CostTime:
    def __init__(self,func):
        self.func = func
    def __call__(self,*args,**kwargs):
        start = time.time()
        result =  self.func(*args, **kwargs)
        end = time.time()
        print(f"耗费时间{end-start}")
        return result

@CostTime
@CacheDecorator
def func1_long_time(*args, **kwargs):
    """模拟耗时较长，每次执行返回结果都一样的情况"""
    print("start func1")
    time.sleep(3)
    print("end func1")
    return 999

if __name__ == '__main__':
   r1 = func1_long_time()
   r2 = func1_long_time()
   print(r1, r2)


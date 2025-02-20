# 多个装饰器_执行顺序的深刻剖析
# 1. 装饰器的执行顺序
# 2. 装饰器的执行顺序的深刻剖析
import time

def mylog(func):
    print("mylog start")
    def inner(*args, **kwargs):
        print("日志记录 start")
        func(*args, **kwargs)
        print("日志记录 end")

    print("mylog end")
    return inner

def cost_time(func):
    print("cost_time start")
    def inners(*args, **kwargs):
        print("开始计时")
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"耗费时间{end-start}")

    print("cost_time end")
    return inners

@mylog
@cost_time #等价于 fun2 = cost_time(fun2)
def fun2():
    print("fun2,start")
    time.sleep(3)
    print("fun2,end")


fun2()

# 上面的代码执行顺序是： 从下往上执行，从里往外执行


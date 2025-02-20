# 装饰器核心_第一个装饰器的写法

#概念：装饰器是一个函数，它的参数是另一个函数，并且它返回一个新的函数。装饰器的本质是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。---

#装饰器的作用：在不改变原函数的情况下，为函数增加新的功能。

def mylog(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print("日志记录")
    return inner


@mylog  #等价于 fun1 = mylog(fun1)
def fun1():
    print("使用功能一")

@mylog  #等价于 fun2 = mylog(fun2)
def fun2(a,b):
    print(f"使用功能二,参数a={a},参数b={b}")


# fun1 = mylog(fun1)
# fun2 = mylog(fun2)

fun1()
fun2(100, 200)
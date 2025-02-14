#闭包实现不修改源码实现添加功能_装饰器的基础(重要)


def outer(func):
    def infunc(*args,**kwargs):
        print("添加功能:日志记录。。。。start")
        func(*args,**kwargs)
        print("添加功能:日志记录。。。。end")
    return infunc

def fun1():
    print("使用功能1")


def fun2(a,b,c,d):
    print("使用功能2",a,b,c,d)

print(id(fun1))
fun1 = outer(fun1)
print(id(fun1),"执行函数赋值后")
fun1()

fun2 = outer(fun2)
fun2(1,2,3,4)
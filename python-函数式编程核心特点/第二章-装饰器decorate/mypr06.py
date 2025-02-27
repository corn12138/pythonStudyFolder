# 类装饰器的典型案例

class Demo:
    def __call__(self, *args, **kwargs):
        print("call方法被调用")

d = Demo()
d() # call方法被调用

#--------------------------------------------------------------

#类装饰器
class myLogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("日志记录")
        return self.func(*args, **kwargs)


@myLogDecorator
def fun2():
    print("使用功能2....")


if __name__ == '__main__':
    fun2()
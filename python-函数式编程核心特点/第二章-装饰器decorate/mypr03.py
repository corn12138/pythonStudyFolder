# 带参数的装饰器典型写法
def mylog(type):
    def decorate(func):
        def inner(*args, **kwargs):
            if type == "文件":
                print("文件:日志记录")
            else:
                print("控制台:日志记录")
            return func(*args, **kwargs)
        return inner
    return decorate

@mylog("文件")
def func2(*args, **kwargs): # *args, **kwargs 代表接受任意数量的参数, 位置参数和关键字参数
    print(f"使用功能2,参数是{args}, {kwargs}")


if __name__ == '__main__':
    func2(100, 200, name="zhangsan", age=20)
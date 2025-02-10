#协程_yield方式实现(了解即可)

import time

def func1():
    for i in range(3):
        print(f"北京：第{i}次打印")
        yield # 通过yield来实现协程,在这里暂停
        time.sleep(1)
    return "func1执行完毕"

def func2():
    g = func1()
    print(type(g))
    for i in range(3):
        print(f"上海：第{i}次打印")
        next(g) # 通过next()方法来执行yield
        time.sleep(1)
    return "func2执行完毕"


def main():
    func1()
    func2()

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"总共耗时：{end_time-start_time}")
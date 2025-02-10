#coding=utf-8
#线程_方法包装创建线程
# 线程：是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。
# 一个进程可以并发多个线程，每个线程并行执行不同的任务。
#栈：线程私有的，存放局部变量
#堆：线程共享的，存放对象
#线程的创建方法：1.直接实例化Thread类 2.继承Thread类 3.方法包装创建线程
import threading
from time import sleep

def fun1(name):
    print(f"线程{name},start")
    for i in range(3):
        print(f"线程:{name},{i}")
        sleep(3)
    print(f"线程{name},end")

if __name__ == '__main__':
    #方法包装创建线程
    print("主线程。start")
    #创建线程
    t1 = threading.Thread(target=fun1,args=("t1",))
    t2 = threading.Thread(target=fun1,args=("t2",))
    #启动线程
    t1.start()
    t2.start()
    print('主线程。end')


# 线程_死锁问题和解决方案
#死锁问题：多个线程同时占用多个资源，但是资源的获取顺序不同


#解决方案：资源的获取顺序统一，或者使用递归锁，或者使用超时时间，或者使用信号量，或者使用条件变量，或者使用线程池，或者使用进程池，或者使用协程，或者使用异步IO

import threading
from time import sleep

def fun1():
    lock1.acquire()
    print("线程1占用资源1")
    sleep(1)
    lock2.acquire()
    print("线程1占用资源2")

    lock2.release()
    print("线程1释放资源2")
    lock1.release()
    print("线程1释放资源1")

def fun2():
    lock2.acquire()
    print("线程2占用资源2")
    sleep(1)
    lock1.acquire()
    print("线程2占用资源1")

    lock1.release()
    print("线程2释放资源1")
    lock2.release()
    print("线程2释放资源2")




if __name__ == '__main__':
    print("主线程开始")
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun2)
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print("主线程结束")
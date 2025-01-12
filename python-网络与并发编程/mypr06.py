#线程_join()和守护线程
#join()方法：等待线程结束,等待线程结束后才会继续执行
#join()方法的使用：t1.join()  t2.join()
#join()方法的作用：等待线程结束
#join()方法的位置：在start()方法之后
#---------------------------------------------------
#守护线程：主线程结束，守护线程也会结束
#守护线程的设置：setDaemon(True)
# 守护线程的设置必须在start()之前
#守护线程 能与join()方法一起使用？--能

import threading
from time import sleep


class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__() #调用父类的构造方法
        self.name = name
    def run(self):
        print(f"线程{self.name},start")
        for i in range(5):
            sleep(3)
            print(f"线程{self.name},i={i}")
        print(f"线程{self.name},end")

if __name__ == '__main__':
    print('主线程,start')
    #创建线程
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    #设置守护线程
    # t1.setDaemon(True)
    # t2.setDaemon(True)
    t1.daemon = True
    t2.daemon = True
    #启动线程
    t1.start()
    t2.start()
    #等待线程结束
    # t1.join()
    # t2.join()
    print('主线程,end')
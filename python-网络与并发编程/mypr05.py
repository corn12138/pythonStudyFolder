#coding=utf-8
#线程_类包装创建线程
import threading
from time import sleep

class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"线程{self.name},start")
        for i in range(3):
            print(f"线程:{self.name},{i}")
            sleep(3)
        print(f"线程{self.name},end")

if __name__ == '__main__':
    #类包装创建线程
    print("主线程，start")
    #创建线程
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    #启动线程
    t1.start()
    t2.start()
    print('主线程，end')
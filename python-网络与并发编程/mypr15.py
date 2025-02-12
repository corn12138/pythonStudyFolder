# 进程_类模式创建进程（继承Process）
from multiprocessing import Process
from time import sleep


class MyProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name
    def run(self):
        print(f"Process:{self.name} start")
        sleep(3)
        print(f"Process:{self.name} end")




if __name__ == '__main__':
    # 创建进程对象
    p1 = MyProcess("p1")
    p2 = MyProcess("p2")
    p3 = MyProcess("p3")
    p1.start()
    p2.start()
    p3.start()
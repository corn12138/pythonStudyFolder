# 进程(process)_方法模式创建进程_windows多进程的一个bug
import os
from multiprocessing import Process
from time import sleep


def fun1(name):
    print(f"fun1，pid:{os.getpid()}")
    print(f"父进程的ID:{os.getppid()}")
    print(f"process {name},start")

    sleep(3)

    print(f"process {name},end")

# 若 没有if __name__ == '__main__': 就会无限制的创建进程
if __name__ == '__main__':
    print("当前进程的id，pid:", os.getpid())
        # 创建进程对象
    p1 = Process(target=fun1, args=("p1",))
    p2 = Process(target=fun1, args=("p2",))
    p1.start()
    p2.start()
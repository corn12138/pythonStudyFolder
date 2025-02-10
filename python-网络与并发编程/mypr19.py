# 进程_进程池管理进程的两种典型案例
#  1. 用进程池管理进程
#  2. 用进程池管理进程，实现进程间通信

from multiprocessing import Pool, Manager
from time import sleep
import os


def func1(name):
    print(f"当前进程的ID：{os.getpid()}，{name}")
    sleep(2)
    return name
def func2(args):
    print(args)

if __name__ == '__main__':

    # pool = Pool(5)
    # # 用进程池管理进程
    # pool.apply_async(func1, args=("进程1",), callback=func2)
    # pool.apply_async(func1, args=("进程2",), callback=func2)
    # pool.apply_async(func1, args=("进程3",), callback=func2)
    # pool.apply_async(func1, args=("进程4",))
    # pool.apply_async(func1, args=("进程5",))
    # pool.apply_async(func1, args=("进程6",))
    # pool.apply_async(func1, args=("进程7",))
    # pool.apply_async(func1, args=("进程8",))
    #
    # pool.close()
    # pool.join()

    # 使用with Pool(5) as pool: 语法糖 代替 pool.close() 和 pool.join()
    with Pool(5) as pool:
        args = pool.map(func1, ["进程1", "进程2", "进程3", "进程4", "进程5", "进程6", "进程7", "进程8"])
        for a in args:
            print(a)

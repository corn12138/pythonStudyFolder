# 进程_Pipe管道实现进程通信
import multiprocessing
from multiprocessing import Process, Pipe, set_start_method, Queue
from time import sleep

def fun1(conn1):
    sub_info = "hello"
    print(f"进程1--{multiprocessing.current_process().pid}发送数据：{sub_info}")
    sleep(1)
    conn1.send(sub_info)
    print(f"来自进程2:{conn1.recv()}")
    sleep(1)

def fun2(conn2):
    sub_info = "你好!!!"
    print(f"进程2--{multiprocessing.current_process().pid}发送数据：{sub_info}")
    sleep(1)
    conn2.send(sub_info)
    print(f"来自进程1:{conn2.recv()}")
    sleep(1)

if __name__ == '__main__':
    #创建管道
    conn1, conn2 = Pipe()
    #创建进程对象
    p1 = Process(target=fun1, args=(conn1,))
    p2 = Process(target=fun2, args=(conn2,))
    p1.start()
    p2.start()
    # join()方法：等待进程结束,等待进程结束后才会继续执行
    p1.join()
    p2.join()


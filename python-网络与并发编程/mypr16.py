# 进程_Queue实现进程通信
from multiprocessing import Queue, Process, set_start_method
from time import sleep


class MyProcess(Process):
    def __init__(self, name,mqs):
        Process.__init__(self)
        self.name = name
        self.mq = mqs
    def run(self):
        print(f"Process:{self.name} start")

        print(f"Process:{self.name} get msg:{self.mq.get()}")
        sleep(5)
        self.mq.put(f"new_data:{self.name}")
        print(f"Process:{self.name} end")


if __name__ == '__main__':
    # try 的作用是为了解决在Mac下使用spawn方法会报错的问题
    try:
        set_start_method("fork")
    except RuntimeError:
        pass
    mq = Queue()
    mq.put("1")
    mq.put("2")
    mq.put("3")

    # 创建进程对象
    # p1 = MyProcess("p1",mq)
    # p2 = MyProcess("p2",mq)
    # p3 = MyProcess("p3",mq)
    # p1.start()
    # p2.start()
    # p3.start()

    #进程列表
    p_list = []
    for i in range(3):
        p = MyProcess(f"p{i}",mq)
        p_list.append(p)
        # p.start()
    for p in p_list:
        p.start()

    # join()方法：等待进程结束,等待进程结束后才会继续执行
    for p in p_list:
        p.join()

    print(mq.get())
    print(mq.get())
    print(mq.get())
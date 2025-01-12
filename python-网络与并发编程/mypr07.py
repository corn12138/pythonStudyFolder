# 线程_全局解释器锁GIL问题
# GIL:全局解释器锁，
# 每个线程在执行的时候，都需要先获取GIL，
# 保证同一时刻只有一个线程在执行，
# 所以GIL会导致多线程无法利用多核优势，
# 只能利用一个核，所以多线程适合I/O密集型，
# 不适合CPU密集型，
# CPU密集型可以使用多进程，
# 每个进程有一个GIL，
# 互不影响，可以利用多核优势，
# 但是进程之间的切换开销比线程大，
# 所以进程适合CPU密集型，线程适合I/O密集型









#--------下边的代码 是上一段python代码的练习
import threading
from time import sleep

class MyThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"线程{self.name},start")
        for i in range(5):
            sleep(2)
            print(f"线程{self.name},i={i}")
        print(f"线程{self.name},end")




if __name__ == '__main__':
    print('主线程,start')
    #创建线程
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    #
    t1.daemon = True
    t2.daemon = True
    #启动线程
    t1.start()
    t2.start()
    #
    # t1.join()
    # t2.join()
    print('主线程,end')
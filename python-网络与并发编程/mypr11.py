#线程_信号量
 # 信号量是一个计数器，每次调用acquire()时-1，调用release()时+1
    # 当计数器为0时，acquire()将阻塞线程直到其他线程调用release()
    # 信号量通常用于限制线程数量，而不是限制访问资源的数量

#应用场景：
    #1.读写文件，一般只能有一个线程在写，但是可以有多个线程在读，这时可以使用信号量来控制
    # 2.爬虫，爬取网页时，为了防止爬取速度过快，可以使用信号量来控制

#底层实现：
    # 1.信号量是基于Condition实现的
    # 2.信号量内部维护了一个Condition对象，通过acquire()和release()来控制线程的执行
    # 3.信号量的计数器是线程安全的，多个线程可以同时调用acquire()和release()方法

from threading import Thread, Semaphore,Lock
from time import sleep

#一个房子，依次只允许两个人进来

def home(name,se):
    se.acquire() #获取信号量
    print(f"{name}进来了")
    sleep(3)
    print(f"*********{name}出去了")
    se.release() #释放信号量



if __name__ == '__main__':
    se = Semaphore(5) #创建信号量对象，设置最大允许的线程数量
    for i in range(7):
        t = Thread(target=home,args=(f"小明{i}",se))
        t.start()
        # join()方法：等待线程结束,等待线程结束后才会继续执行
        # t.join()


# 线程_事件Event对象


# 事件Event ：主要用于唤醒正在阻塞等待的线程
# 原理：Event对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。在初始状态下，Event对象中的信号标志被设置为假。如果有线程等待一个Event对象，而这个Event对象的标志为假，那么这个线程将会被一直阻塞，直至另一个线程将这个Event对象的标志设置为真。一个线程如果等待一个已经被设置为真的Event对象，那么它将忽略这个事件，继续执行。

# Event对象的方法：
#Event.wait(timeout=None)：阻塞线程，直至Event对象的信号标志为真
# Event.set()：将Event对象的信号标志设置为真
# Event.clear()：将Event对象的信号标志设置为假
# Event.isSet()：返回Event对象的信号标志状态。如果信号标志为真，返回True；否则返回False


import threading
import time

def chihuoguo(name, event):
    print(f"{name}已经启动")
    print(f"小伙伴{name}已经进入就餐状态！")
    time.sleep(1)
    event.wait()  # 等待事件，进入阻塞状态
   #收到事件后进入运行状态
    print(f"{name}收到通知了")
    print(f"小伙伴{name}开始吃")



if __name__ == '__main__':
    event = threading.Event()  # 创建事件对象
    # 创建多个线程
    thread1 = threading.Thread(target=chihuoguo, args=("小明", event))
    thread2 = threading.Thread(target=chihuoguo, args=("小红", event))
    # 启动线程
    thread1.start()
    thread2.start()

    time.sleep(10)
    #发送事件
    print("->>>>>>>>>>>>>>>>>>>>>>>主线程发送事件")
    event.set()  # 发送事件通知

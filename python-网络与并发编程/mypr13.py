#线程_生产者消费者模式

from queue import Queue
from threading import Thread # 这是一个线程模块
from time import sleep

def producer():
    num = 1
    while True:
        if queue.qsize() < 5:
            print(f"生产者生产了{num}号，馒头")
            queue.put(f"{num}号馒头")
            num += 1
        else:
            print("馒头库存已满，等待消费者消费")
        sleep(2)

def consumer():
    while True:
        if queue.qsize() > 0:
            print(f"消费者消费了{queue.get()}")
        else:
            print("馒头库存不足，等待生产者生产")
        sleep(1)

if __name__ == '__main__':
    queue = Queue(5)
    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)
    t1.start()
    t2.start()
    # join()方法：等待线程结束,等待线程结束后才会继续执行
    # t1.join()
    # t2.join()

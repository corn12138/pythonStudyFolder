# 线程_互斥锁典型案例
# 互斥锁：同一时刻只能有一个线程访问共享数据,
# 互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享数据
# 必须使用同一个锁对象，才能保证互斥
#互斥锁的作用就是保证同一时刻只有一个线程访问共享数据；保证共享数据不会出现错误问题
#使用互斥锁的好处确保某段关键代码只能由一个线程从头到尾完整地执行，其他线程不得干扰
#使用互斥锁会影响代码的执行效率，因为只能一个线程执行，其他线程需要等待
#同时持有多把锁，容易发生死锁，导致程序无法执行

# 注意：互斥锁是多个线程一起去抢，抢到锁的线程才能执行，没有抢到的线程需要等待，直到抢到锁的线程释放锁，其他线程才能继续抢
# 互斥锁的释放：1、自动释放 2、手动释放
# 互斥锁的手动释放：1、acquire() 2、release()
# 互斥锁的自动释放：1、acquire() 2、release() 3、with语句

import threading
from time import sleep as sl, clock_settime

class Account:
    def __init__(self,money,name):
        self.money = money
        self.name = name

class Drawing(threading.Thread):
    def __init__(self,drawingNum,account,lock):
        super().__init__()
        self.drawingNum = drawingNum
        self.account = account
        self.expenseTotal = 0
        self.lock = lock

    def run(self):
        # 获取锁
        lock.acquire()
        if self.account.money<self.drawingNum:
            print('余额不足',end=' ')
            return
        sl(1) # 判断完可以取钱，则阻塞，就是为了测试发生资源冲突
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum
        # 释放锁
        lock.release()
        print(f"账户：{self.account.name}，余额：{self.account.money}，本次取款：{self.drawingNum}，总取款：{self.expenseTotal}")


if __name__ == '__main__':
    a1 =Account(1000,'a1')
    # 创建锁
    lock = threading.Lock()
    drawing1 = Drawing(800,a1,lock)
    drawing2 = Drawing(800,a1,lock)
    # 两个线程同时取钱，会发生资源冲突
    drawing1.start()
    drawing2.start()

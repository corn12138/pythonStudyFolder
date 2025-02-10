# 线程_线程同步和互斥锁_资源冲突案例
# 两个线程同时取钱，会发生资源冲突
# 互斥锁：解决资源冲突问题
# 互斥锁的使用：创建锁，上锁，解锁
# 互斥锁的好处：保证了多线程的安全性
# 互斥锁的坏处：降低了程序的效率
# 互斥锁的原理：当一个线程上锁时，其他线程会等待，直到解锁

from threading import Thread #导入线程模块
from time import sleep


class Account:
    def __init__(self,money,name):
        self.money = money
        self.name = name


# 模拟 提款操作
class Drawing(Thread):
    def __init__(self,drawingNum,account):
        Thread.__init__(self) #调用父类的构造方法
        self.drawingNum = drawingNum
        self.account = account
        self.expenseTotal = 0

    def run(self):
        if self.account.money < self.drawingNum:
            return
        sleep(1) #判断完可以取钱，则阻塞，就为了 测试发生资源冲突
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum
        print(f"账户：{self.account.name}--余额是：{self.account.money}")
        print(f"账户：{self.account.name}--总共取了：{self.expenseTotal}")


if __name__ == '__main__':
    a1 = Account(100,'a1')

    draw1 = Drawing(50,a1)
    draw2 = Drawing(60,a1)

    draw1.start()
    draw2.start()
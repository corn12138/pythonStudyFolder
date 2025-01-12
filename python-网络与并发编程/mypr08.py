# 线程_线程同步和互斥锁_资源冲突案例

import threading
from time import sleep as sl

class Account:
    def __init__(self,money,name):
        self.money = money
        self.name = name


class Drawing(threading.Thread):
    def __init__(self,drawingNum,account):
        super().__init__()
        self.drawingNum = drawingNum
        self.account = account
        self.expenseTotal = 0

    def run(self):
        if self.account.money<self.drawingNum:
            print('余额不足',end=' ')
            return
        sl(1) # 判断完可以取钱，则阻塞，就是为了测试发生资源冲突
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum
        print(f"账户：{self.account.name}，余额：{self.account.money}，本次取款：{self.drawingNum}，总取款：{self.expenseTotal}")

if __name__ == '__main__':
    a1 =Account(1000,'a1')

    drawing1 = Drawing(800,a1)
    drawing2 = Drawing(800,a1)
    # 两个线程同时取钱，会发生资源冲突
    drawing1.start()
    drawing2.start()
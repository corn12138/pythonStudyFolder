# UDP编程4_多线程结合自由通信

#UDP实现多线程服务端

from socket import *  # 导入socket模块
from threading import Thread  # 导入多线程模块

def recv_data():
    while True:
        recv_data = s.recvfrom(1024)  # 1024表示本次接收的最大字节数
        recv_content = recv_data[0].decode("gbk")
        print(f"接收到的数据为：{recv_content} from {recv_data[1]}")
        if recv_content == "88":
            print("通信结束")
            break

def send_data():
    addr = ("127.0.0.1",8888)
    while True:
        data = input("请输入要发送的数据：")
        s.sendto(data.encode("gbk"),addr)  # 发送数据
        if data == "88":
            print("通信结束")
            break





if __name__ == '__main__':
    s = socket(AF_INET,SOCK_DGRAM)  # 创建UDP套接字
    s.bind(("127.0.0.1",9999))  # 绑定地址和端口--这里的端口号要和客户端的端口号一致
    # 创建两个线程
    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    # join()方法：等待线程结束,等待线程结束后才会继续执行
    t1.join()
    t2.join()

    # s.close()  # 关闭套接字

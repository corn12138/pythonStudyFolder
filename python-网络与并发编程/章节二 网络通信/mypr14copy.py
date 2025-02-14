# TCP编程4_结合多线程实现自由通信

# 客户端

from socket import *  # 导入socket模块
from  threading import Thread

def recv_data():
    while True:
        #接收服务端数据
        recv_data=client_socket.recv(1024) # 1024表示本次接收的最大字节数
        recv_content = recv_data.decode("gbk")
        print(f"服务端说：{recv_content}")
        if recv_content == "end":
            break

def send_data():
    while True:
        send_data = input(">")
        client_socket.send(send_data.encode("gbk"))  # 发送数据
        if send_data == "end":
            break


if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字
    client_socket.connect(("127.0.0.1",8900)) # 连接服务器

    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    client_socket.close()  # 关闭套接字
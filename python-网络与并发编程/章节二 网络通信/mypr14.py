# TCP编程4_结合多线程实现自由通信

# 服务端

from socket import *  # 导入socket模块
from threading import Thread

def recv_data():
    while True:
        recv_data = client_socket.recv(1024)  # 1024表示本次接收的最大字节数
        recv_content = recv_data.decode("gbk")
        print(f"客户端说：{recv_content} from {client_info}")
        if recv_content == "end":
            break


def send_data():
    while True:
        msg = input(">")
        client_socket.send(msg.encode("gbk"))
        if msg == "end":
            break

if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字
    server_socket.bind(("127.0.0.1",8900)) # 绑定地址(本机)和端口
    server_socket.listen(5)  # 监听端口
    print("等待接收连接...")
    client_socket,client_info = server_socket.accept()  # 接收客户端的连接请求--->这个写法 左边是两个变量，右边是一个元组
    print("一个客户端连接成功")

    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    client_socket.close()  # 关闭客户端套接字
    server_socket.close()  # 关闭服务器套接字
# TCP编程3_服务端和客户端持续通信

#客户端

from socket import *  # 导入socket模块

client_socket = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字
client_socket.connect(("127.0.0.1",8900)) # 连接服务器

while True:
    send_data = input(">")
    client_socket.send(send_data.encode("gbk"))  # 发送数据
    if send_data == "end":
        break
    #接收服务端数据
    recv_data=client_socket.recv(1024) # 1024表示本次接收的最大字节数
    print(f"服务端说：{recv_data.decode('gbk')}")

client_socket.close()  # 关闭套接字
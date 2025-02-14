# TCP编程3_服务端和客户端持续通信

# 服务端

from socket import *  # 导入socket模块

server_socket = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字
server_socket.bind(("127.0.0.1",8900)) # 绑定地址(本机)和端口
server_socket.listen(5)  # 监听端口
print("等待接收连接...")
client_socket,client_info = server_socket.accept()  # 接收客户端的连接请求--->这个写法 左边是两个变量，右边是一个元组
print("一个客户端连接成功")
while True:
    recv_data = client_socket.recv(1024)  # 1024表示本次接收的最大字节数
    recv_content = recv_data.decode("gbk")
    print(f"客户端说：{recv_content} from {client_info}")
    if recv_content == "end":
        break
    msg = input(">")
    client_socket.send(msg.encode("gbk"))

client_socket.close()  # 关闭客户端套接字
server_socket.close()  # 关闭服务器套接字
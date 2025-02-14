# TCP编程1_服务器端简化代码

from socket import *  # 导入socket模块

server_socket = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字
server_socket.bind(("127.0.0.1",8899)) # 绑定地址(本机)和端口
server_socket.listen(5)  # 监听端口

print("等待接收连接...")

client_socket,client_info = server_socket.accept()  # 接收客户端的连接请求--->这个写法 左边是两个变量，右边是一个元组
recv_data = client_socket.recv(1024)  # 1024表示本次接收的最大字节数
print(f"收到信息：{recv_data.decode('gbk')} from {client_info}")

client_socket.close()  # 关闭客户端套接字
server_socket.close()  # 关闭服务器套接字

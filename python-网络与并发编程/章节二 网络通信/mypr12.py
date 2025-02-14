# TCP编程2_客户端经简化代码

from socket import *  # 导入socket模块

client_scoket = socket(AF_INET, SOCK_STREAM)  # 创建TCP套接字

client_scoket.connect(("127.0.0.1", 8899))  # 连接服务器

client_scoket.send("你好，我是客户端".encode("gbk"))  # 发送数据

client_scoket.close()  # 关闭套接字
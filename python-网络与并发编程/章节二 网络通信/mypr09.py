# UDP编程3_持续通信

from socket import *  # 导入socket模块

s = socket(AF_INET,SOCK_DGRAM)  # 创建UDP套接字

s.bind(("127.0.0.1",8888))  # 绑定地址和端口
print("等待接收数据...")

while True:
    recv_data = s.recvfrom(1024)  # 1024表示本次接收的最大字节数
    recv_content = recv_data[0].decode("gbk")
    print(f"接收到的数据为：{recv_content} from {recv_data[1]}")
    if recv_content == "88":
        print("通信结束")
        break

s.close()  # 关闭套接字
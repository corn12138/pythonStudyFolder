# UDP编程2_客户端发送数据经典案例
# 最简化的UDP客户端发送数据的经典案例

from socket import * # 导入socket模块

s = socket(AF_INET, SOCK_DGRAM) # 创建UDP套接字

addr = ("127.0.0.1",8888) # 服务器的地址和端口
while True:
    data = input("请输入要发送的数据：")
    s.sendto(data.encode("gbk"),addr) # 发送数据
    if data == "88":
        print("通信结束")
        break
s.close() # 关闭套接字


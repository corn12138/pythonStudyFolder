# UDP编程1_服务器接收数据经典案例
# 最简化的UDP服务器端接收数据的经典案例

from socket import * # 导入socket模块

s = socket(AF_INET, SOCK_DGRAM) # 创建UDP套接字
s.bind(("127.0.0.1", 8888)) # 绑定地址和端口
print("等待接收数据...")
recv_data=s.recvfrom(1024) #1024表示本次接收的最大字节数
print(f"接收到的数据为：{recv_data[0].decode('gbk')} from {recv_data[1]}")
s.close() # 关闭套接字



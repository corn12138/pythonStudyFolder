# 二进制表示中频率为1的数量统计
num = 100
print(bin(num)) #bin 二进制表示
#旧版本

print('出现1的次数:',bin(num).count('1'))




#新版本
print('出现1的次数:',num.bit_count()) #bit_count() 是 Python 3.10 引入的一个整数方法，用于统计一个整数的二进制表示中位值为 1 的个数（也称为汉明权重）。
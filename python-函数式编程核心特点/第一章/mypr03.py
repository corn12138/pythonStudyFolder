# 偏函数
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数

# python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
# 偏函数的作用就是把一个函数的某些参数固定住，返回一个新的函数，调用这个新函数会更简单

#eg：
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换

import functools

def int2(x,base=2):
    return int(x,base)

print(int2('1000000')) # 64
print(int2('1000000',base=10)) # 100

int3 = functools.partial(int,base=2)
print(int3('1000000')) # 64
print(int3('1000000',base=10)) # 100

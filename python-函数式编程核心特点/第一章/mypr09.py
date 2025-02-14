#reduce函数的使用
# reduce 的使用方法：reduce(function, iterable[, initializer])----function是一个函数，iterable是一个可迭代对象，initializer是一个初始值

from functools import reduce

def add(x,y):
    return x+y

sum = reduce(add,range(1,101),0)
print(sum)
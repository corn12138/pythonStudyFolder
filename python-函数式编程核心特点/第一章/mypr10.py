#filter函数的使用
# filter: 过滤函数，对可迭代对象进行过滤，返回一个filter对象,传入的参数是一个函数和一个可迭代对象，返回值是一个filter对象
# filter对象是一个可迭代对象，可以转换成list或者set

def is_odd(n):
    return n % 2 == 1

l = filter(is_odd,range(10))
print(list(l))

l = filter(lambda x:x%2==1,range(10))
print(list(l))
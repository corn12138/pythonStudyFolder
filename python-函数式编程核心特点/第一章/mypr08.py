# map函数的使用
 # map接收一个函数和一个序列，将函数作用于序列的每一个元素，返回一个迭代器
 #通俗地说，就是将序列中的每一个元素都传递给函数，然后将函数的返回值作为一个新的迭代器返回

def f(x):
    return x**2
L = []
for i in range(10):
    L.append(f(i))
print(L)
"""
map函数的使用
"""
def g(x):
    return x**2
L = list(map(g,range(10)))
print(L)
# 或者
L = map(lambda n:n**2,range(12))
print(list(L))

"""
map传多个序列
"""

def f2(x,y):
    return x + y

ls = list(map(f2,[1,2,3,4],[5,6,7,8]))
print(ls)

ls = list(map(lambda x,y:x+y,range(1,4),range(5,7)))
print(ls)


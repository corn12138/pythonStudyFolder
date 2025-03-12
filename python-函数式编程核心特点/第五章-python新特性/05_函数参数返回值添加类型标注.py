#定于一个函数
#参数 num int类型
#返回值 字符串类型
def num_fun(num) ->str:
    return str(num)

print(num_fun(10))
print(num_fun('hello'))

#
def sum_fun(a:int,b:int)->int:
    return a+b
# 定义参数默认值
def fun_test(num1:int=10,num2:int=20)->int:
    return num1+num2

#定义变量 指向一个函数
from  typing import Callable

# Callable[[int,int],int] 表示接收两个int类型参数，返回值为int类型
f:Callable[[int,int],int] = sum_fun

print(f(10,20))

# 定义函数，产生整数的生成器，每次返回一个
from typing import Iterator
# Iterator[int] 表示返回值是一个整数的生成器
def return_fun(num:int)->Iterator[int]:
    i = 0
    while i < num:
        yield i
        i += 1

print(return_fun(10))

for i in return_fun(10):
    print(i)
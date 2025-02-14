# lambda表达式和匿名函数
# lambda表达式是一个匿名函数，可以接受任意多个参数，并且返回单个表达式的值
# lambda表达式的语法格式如下：
# lambda 参数1, 参数2, ... : 表达式
# lambda x, y: x + y
# 该lambda表达式接受两个参数，返回这两个参数的和
f = lambda x, y: x + y
print(f(10, 20))  # 30
print(f,type(f),id(f))

g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]

print(g[0](3)) # 调用第一个lambda表达式，传入参数3，返回3*2=6
print(g[1](3)) # 调用第二个lambda表达式，传入参数3，返回3*3=9
print(g[2](3)) # 调用第三个lambda表达式，传入参数3，返回3*4=12


#函数式编程总体介绍
 #函数式编程是一种编程范式，它将计算机运算视为数学函数的计算，并且避免了状态以及可变数据。


#高阶函数和内存分析_可变参数的传递处理
#函数式编程最鲜明的特征就是函数是第一等公民，函数可以作为参数传递，函数可以作为返回值返回

#高阶函数：函数的参数是函数，函数的返回值是函数。（一个函数可以 接收另外一个函数作为参数，那么这种函数称之为高阶函数）
#内存分析：函数的内存分析，函数的参数传递，函数的返回值传递
#可变参数的传递处理：*args,**kwargs --args是一个元组，kwargs是一个字典
# python的内建高阶函数：map,filter,reduce,sorted

def test():
    print("test function is running!!!")

def test2(func,*args,**kwargs):
    print("test2 function is running!!!")
    func(*args,**kwargs)


def test3(a,b):
    print(f"test3 ,{a},{b}")

a = test # 函数名可以作为变量赋值给其他变量
# test2(a)
test2(test3,100,200)

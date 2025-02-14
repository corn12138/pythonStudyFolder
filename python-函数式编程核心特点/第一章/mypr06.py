#闭包和自由变量_全局变量污染问题的解决

"""
下边的例子中，a这个全局变量被add函数修改了，导致print_num函数的判断条件不成立，这就是全局变量污染的问题。
"""
a = 10
def add():
    global a
    a += 1
    print(a)

def print_num():
    if a == 10:
        print("a的值是10")
    else:
        print("a的值不是10")

add()
print_num()

"""
下边的例子中， 全局变量a虽然 没有被更改，但是也没有实现 a的累加
"""
a = 10
def add():
    a = 10
    a += 1
    print(a)

def print_num():
    if a == 10:
        print("a的值是10")
    else:
        print("a的值不是10")

add()
add()
add()
print_num()


"""
下边的例子中，通过闭包的方式解决了全局变量污染的问题
"""
b = 10
def add ():
    b = 10
    def increment():
        nonlocal b
        b += 1
        print(f"b:{b}")
    return increment

def print_num():
    if b == 10:
        print("b的值是10")
    else:
        print("b的值不是10")

increment = add()
increment()
increment()
increment()
print_num()

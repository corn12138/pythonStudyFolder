# 闭包的内存分析(重要)

def outer():
    a = 10
    def inner():
        nonlocal a
        print(a)
        a += 1
    return inner

inn = outer()
inn()
inn()
inn()
inn()

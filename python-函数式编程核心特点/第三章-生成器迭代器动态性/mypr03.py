# 生成器函数_send的用法

def test():
    print("start")
    i = 0
    while i < 2:
        temp = yield i
        print(f"temp = {temp}")
        i += 1
    print("end")


if __name__ == '__main__':
    g = test()
    print(next(g))
    print("------")
    print(g.send(100))
    print(next(g))

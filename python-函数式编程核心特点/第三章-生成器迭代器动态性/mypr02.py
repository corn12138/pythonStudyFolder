# 生成器函数_yield的用法


def test(*args, **kwargs):
    """
    生成器函数
    :param args:
    :param kwargs:
    :return:
    1.函数有了yield之后，调用它，就会生成一个生成器
    2.yield作用，程序挂起，返回相应的值。下次从下一个语句开始执行。(注意 不是下一行的语句)
    3.return在生成器中代表生成器结束，如果return后面有值，会抛出StopIteration异常
    4.next() 与 __next__() 作用一样,唤醒并继续执行
    """
    print("start")
    i = 0
    while i < 3:
        # yield i
        temp = yield i
        print(f"temp = {temp}")
        print(f"i = {i}")
        i += 1
    print("end")
    return "done"


if __name__ == '__main__':
    t = test()
    t.__next__()
    t.__next__()
    t.__next__()
    # t.__next__()
    # try:
    #     t.__next__()
    #
    # except StopIteration as e:
    #     print(e.value)


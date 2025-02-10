#协程_syncio异步IO实现协程

# 1.正常的函数执行时是不会中断的，所以需要写一个能够中断的函数，需要加async


import asyncio
import time

async def func1():
    for i in range(3):
        print(f"北京：第{i}次打印")
        await asyncio.sleep(1) # 通过await来实现协程,在这里暂停
    return "func1执行完毕"

async def func2():
    for i in range(3):
        print(f"上海：第{i}次打印")
        await asyncio.sleep(1)
    return "func2执行完毕"

async def main():
    res = await asyncio.gather(func1(),func2()) # gather()方法可以同时执行多个协程
    print(res)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"总共耗时：{end_time-start_time}")

# 进程_Manager管理器实现进程通信

from multiprocessing import Process, Manager,current_process

def func(name,m_list,m_dict):
    m_dict['name'] = 'sxt'
    m_list.append("你好！！！")


if __name__ == '__main__':
    with Manager() as mgr: #创建一个管理器,with语句结束后，管理器也会关闭
        m_list = mgr.list() #创建一个列表
        m_dict = mgr.dict() #创建一个字典
        m_list.append("hello") #往列表中添加元素
        #两个进程不能直接互相使用对象，需要互相传递
        p1 = Process(target=func,args=("p1",m_list,m_dict))
        p1.start()
        p1.join() #等待进程结束
        print(f"主进程{m_list}")
        print(f"主进程{m_dict}")
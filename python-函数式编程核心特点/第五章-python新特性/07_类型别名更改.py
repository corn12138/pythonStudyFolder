#旧版本
oldstr = str
msg:oldstr = 'hello'

print(msg)




#新版本
from typing import TypeAlias

# 定义类型别名
newstr :TypeAlias = str
newint :TypeAlias = int

def func_test(num:newint,msg:newstr)->newstr:
    return str(num) + msg

print(func_test(10,msg='hello'))
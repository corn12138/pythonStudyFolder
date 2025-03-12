# re模块_findall_finditer与sub的使用

import re

# 提取 findall返回的是一个列表,里面是所有匹配的结果
o=re.findall(r'\d+','abc123def456')   #['123', '456']
print(o)

# 提取二- finditer返回的是一个迭代器，可以用for循环遍历,返回的是一个迭代器，finditer函数的第一个参数是正则表达式，第二个参数是要匹配的字符串
p=re.finditer(r'\d+','abc123def456')   #<callable_iterator object at 0x0000021D3D3A3D30>
for i in p:
    print(f"i:{i},i.group():{i.group()}")

# 提取三- sub替换，将匹配到的内容替换为指定的内容,返回的是一个字符串(原字符串 ),sub函数的第一个参数是正则表达式，第二个参数是要替换的内容，第三个参数是要匹配的字符串
q=re.sub(r'\d+','***','abc123def456')   #'abc***def***'
print(q)
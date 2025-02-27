# re模块_match与search的使用

import re
#匹配 match是从字符串的开头开始匹配，如果开头不匹配，就不会继续往下匹配
m=re.match(r'\d+','123abc')
print(f"match,{m}")   #<re.Match object; span=(0, 3), match='123'>

#搜索 search是搜索整个字符串，只要有一个匹配就返回
n=re.search(r'\d+','abc123')   #<re.Match object; span=(3, 6), match='123'>
print(f"search,n:{n},n.group():{n.group()}")

#提取 findall返回的是一个列表,里面是所有匹配的结果
o=re.findall(r'\d+','abc123def456')   #['123', '456']
print(o)

# 提取二- finditer返回的是一个迭代器，可以用for循环遍历
p=re.finditer(r'\d+','abc123def456')   #<callable_iterator object at 0x0000021D3D3A3D30>
for i in re.finditer(r'\d+','abc123def456'):
    print(f"i:{i},i.group():{i.group()}")

# 提取三- sub替换，将匹配到的内容替换为指定的内容
re.sub(r'\d+','***','abc123def456')   #'abc***def***'




def test_regexp(pattern,strings):
    for s in strings:
        if re.fullmatch(pattern,s):
            print(f"匹配到的 {s}")
        else:
            print(f"匹配失败的:{s}")


test_strings = ['bat','bit', 'but', 'hat', 'hit', 'hut']

pattern = r'[bh][aiu]t' # 非贪婪模式

test_regexp(pattern,test_strings)

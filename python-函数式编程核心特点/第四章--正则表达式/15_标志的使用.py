# 标志的使用

# re.I 忽略大小写
# re.M 多行匹配
# re.S 单行匹配,目的是使 . 匹配包括换行符在内的所有字符
# re.U 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X 详细模式。忽略空格和注释。使得你可以把正则表达式写得更美观。

import re

# re.I 忽略大小写
print(f"{'_'*20}re.I 忽略大小写{'_'*20}")
m = re.match(r'[a-z]+','Python is the best language',re.IGNORECASE)
if m:
    print(f"m:{m.group()}")
else:
    print(f"m 没有匹配到")

# re.S 单行匹配 -- 他的作用是使 . 匹配包括换行符在内的所有字符
print(f"{'_'*20}re.S 单行匹配{'_'*20}")

m1 = re.match(r'.+','Python is the best \n language',re.S)
if m1:
    print(f"m1:{m1.group()}")
else:
    print(f"m1 没有匹配到")

#re.X 详细模式, 忽略空格和注释
print(f"{'_'*20}re.X 详细模式{'_'*20}")
m2 = re.match(r"""
    ^ # 匹配开头
    ( # 分组1
        [a-z]+[A-Z]+ # 匹配字母,大小写
        | # 或
        [A-Z]+[a-z]+ # 匹配字母
    ) # 分组1结束
    \s # 匹配空白
    (Python) # 匹配Python,分组2
    ""","Hello Python",re.X)
if m2:
    print(f"m2:{m2.group()}")
else:
    print(f"m2 没有匹配到")
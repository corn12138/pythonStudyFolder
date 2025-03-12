# 匹配单个字符演示1
import re

# 匹配单个字符介绍
# 精准匹配
print(f"精准匹配:{'*'*20}")

m = re.match('test','test python re')
print(f"m:{m.group()}")  #test

#特殊匹配
print(f"特殊匹配:{'*'*20}")
m1 = re.match(r'\$test','$test python re')
print(f"m1:{m1.group()}")  #None

#匹配字符
    # . 匹配任意字符(除了\n)
print(f". 匹配任意字符(除了\n):{'*'*20}")
m2 = re.match('.','test python re')
print(f"m2:{m2.group()}")  #t

m3 = re.match('te.t','test')
print(f"m3:{m3.group()}")  #test

# [] 匹配[]中的任意一个字符
print(f"[] 匹配[]中的任意一个字符:{'*'*20}")
m4 = re.match('[a-z]','test')
print(f"m4:{m4.group()}")  #t

m5 = re.match('[h]','hello python')
print(f"m5:{m5.group()}")  #h

m6 = re.match('[hH]','Hello python')
print(f"m6:{m6.group()}")  #H

m7 = re.match('[0-9]','6hello python')
print(f"m7:{m7.group()}")  #6

m8 = re.match('[a-z0-9A-Z]','h6ello python')
print(f"m8:{m8.group()}")  #h

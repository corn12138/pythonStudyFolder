# 匹配多个字符演示2
import re

# + 匹配前一个字符1次或无限次
m1 = re.match(r"p.+n", "python")
if m1:
    print(f"m1:{m1.group()}")  #h
else:
    print(f"m1 没有匹配到")

m2 = re.match(r"p.+n", "p1n") # . 是匹配任意字符
if m2:
    print(f"m2:{m2.group()}")  #python
else:
    print(f"m2 没有匹配到")

# ? 匹配前一个字符0次或1次
m3 = re.match(r"http?", "httpp") # . 是匹配任意字符
if m3:
    print(f"m3:{m3.group()}")  #pn
else:
    print(f"m3 没有匹配到")

m4 = re.match(r"https?", "http")
if m4:
    print(f"m4:{m4.group()}")  #http
else:
    print(f"m4 没有匹配到")
# {m} 匹配前一个字符m次
m5 = re.match(r"\w{4}", "python")
if m5:
    print(f"m5:{m5.group()}")  #ppp
else:
    print(f"m5 没有匹配到")

# {m,} 匹配前一个字符m到无限次
m6 = re.match(r"\w{4,}", "python09u有关于鱼骨辫一个预告一个iu不好预感")
if m6:
    print(f"m6:{m6.group()}")  #python
else:
    print(f"m6 没有匹配到")
# {,n} 匹配前一个字符0到 n次
m7 = re.match(r"\w{,5}", "python")
if m7:
    print(f"m7:{m7.group()}")  #pyth
else:
    print(f"m7 没有匹配到")

# {m,n} 匹配前一个字符m到n次
m8 = re.match(r"\w{4,6}", "python")
if m8:
    print(f"m8:{m8.group()}")  #pytho
else:
    print(f"m8 没有匹配到")

m9 = re.match(r"\w{8,10}", "1a2b3c4d5e6f7g8h9i0jklmn")
if m9:
    print(f"m9:{m9.group()}")  #pythons
else:
    print(f"m9 没有匹配到")
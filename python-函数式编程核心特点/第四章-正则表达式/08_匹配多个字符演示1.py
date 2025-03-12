# 匹配多个字符演示1
import re

# * 匹配前一个字符0次或无限次
print(f"{'_'*20}","* 匹配前一个字符0次或无限次",f"{'_'*20}")
m1 = re.match(r"h*", "hfhsssdhsa")
if m1:
    print(f"m1:{m1.group()}")  #h
else:
    print(f"m1 没有匹配到")

m2 = re.match(r"h*", "hhfhsssdhsa")
if m2:
    print(f"m2:{m2.group()}")  #
else:
    print(f"m2 没有匹配到")

m3 = re.match(r"\w*", "fhsssdhsa")
if m3:
    print(f"m3:{m3.group()}")  #fhsssdhsa
else:
    print(f"m3 没有匹配到")

m4 = re.match(r"\w*", "fhsssdhsa world")
if m4:
    print(f"m4:{m4.group()}")  #fhsssdhsa
else:
    print(f"m4 没有匹配到")

m5 = re.match(r"\w*\s\w*", "fhsssdhsa world")
if m5:
    print(f"m5:{m5.group()}")  #fhsssdhsa world
else:
    print(f"m5 没有匹配到")

m6 = re.match(r"\s*\w*", " \tfhsssdhsa world")
if m6:
    print(f"m6:{m6.group()}")  #
else:
    print(f"m6 没有匹配到")
print(m6)

m7 = re.match(r"[\s\w]*", " \tfhsssdhsa world")
if m7:
    print(f"m7:{m7.group()}")  #
else:
    print(f"m7 没有匹配到")

# + 匹配前一个字符1次或无限次
m8 = re.match(r"h+", "hfhsssdhsa")
if m8:
    print(f"m8:{m8.group()}")  #h
else:
    print(f"m8 没有匹配到")
# ? 匹配前一个字符0次或1次

# {m} 匹配前一个字符m次

# {m,} 匹配前一个字符m到无限次

# {,n} 匹配前一个字符0到 n次

# {m,n} 匹配前一个字符m到n次
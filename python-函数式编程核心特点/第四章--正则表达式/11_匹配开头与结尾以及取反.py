# 匹配开头与结尾以及取反
import re

#匹配开通 ^
print(f"匹配开头:{'*'*20}")
m1 = re.match(r'^\d.+','2python2停止维护了')
if m1:
    print(f"m1:{m1.group()}")
else:
    print(f"m1 没有匹配到")

#匹配结尾 $
print(f"匹配结尾:{'*'*20}")
m2 = re.match(r'.+\d$','python2停止维护了2')
if m2:
    print(f"m2:{m2.group()}")
else:
    print(f"m2 没有匹配到")

m3 = re.match(r'.+\d$','python2停止维护了5o')
if m3:
    print(f"m3:{m3.group()}")
else:
    print(f"m3 没有匹配到")

# 匹配开头与结尾
print(f"匹配开头与结尾:{'*'*20}")
m4 = re.match(r'^\d.*\d$','2python2停止维护了2')
if m4:
    print(f"m4:{m4.group()}")
else:
    print(f"m4 没有匹配到")

# ^ 取反功能
print(f"取反功能:{'*'*20}")
m5 = re.match(r'[^abcd].+','python2停止维护了2')
if m5:
    print(f"m5:{m5.group()}")
else:
    print(f"m5 没有匹配到")

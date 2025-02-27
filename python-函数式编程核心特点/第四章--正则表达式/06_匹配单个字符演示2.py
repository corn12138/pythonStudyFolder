# 匹配单个字符演示2

import  re # 导入re模块

# \d 匹配数字, 0-9
print(f"匹配数字:{'*'*20}")
print(f" 匹配非数字:{'*'*20}")
m = re.match('python2','python2停止维护了')

#精准匹配
if m:
    print(f"m:{m.group()}")
else:
    print(f"m 没有匹配到")
#
m2 = re.match(r'python\d','python2停止维护了')
if m2:
    print(f"m2:{m2.group()}")
else:
    print(f"m2 没有匹配到")

# \D 匹配非数字
print(f"匹配非数字:{'*'*20}")
m3 = re.match(r'python\D','python?o停止维护了')
if m3:
    print(f"m3:{m3.group()}")
else:
    print(f"m3 没有匹配到")

# \s 匹配空白,空格,tab键
print(f" 匹配空白,空格,tab键:{'*'*20}")
m4 = re.match(r'python\stest','python test停止维护了')
if m4:
    print(f"m4:{m4.group()}")
else:
    print(f"m4 没有匹配到")

# /t 匹配tab键
m5 = re.match(r'python\ttest','python\ttest停止维护了')
if m5:
    print(f"m5:{m5.group()}")
else:
    print(f"m5 没有匹配到")

# \S 匹配非空白
print(f"匹配非空白:{'*'*20}")
m6 = re.match(r'python\Stest','python[]test')
if m6:
    print(f"m6:{m6.group()}")
else:
    print(f"m6 没有匹配到")

# \w 匹配 单词字符,字母,数字,下划线
print(f"匹配 单词字符,字母,数字,下划线:{'*'*20}")
m7 = re.match(r'\w','&python2停止维护了')
if m7:
    print(f"m7:{m7.group()}")
else:
    print(f"m7 没有匹配到")
# \W 匹配非单词字符
print(f"匹配非单词字符:{'*'*20}")
m8 = re.match(r'\W','¥$python2停止维护了')
if m8:
    print(f"m8:{m8.group()}")
else:
    print(f"m8 没有匹配到")


# 匹配任意数据 [\d\D] [\s\S] [\w\W]
print(f"匹配任意数据:{'*'*20}")
m9 = re.match(r'[\d\D]','python2停止维护了')
if m9:
    print(f"m9:{m9.group()}")
else:
    print(f"m9 没有匹配到")
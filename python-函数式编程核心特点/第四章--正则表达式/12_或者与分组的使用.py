# 或者与分组的使用
import re

# 1. ｜ 或者
print("______________________1. ｜ 或者______________________")
skill_list = ["python","msql","flask","django","php"]

for value in skill_list:
    m1 = re.match('python|flask',value)
    if m1:
        print(f"m1:{m1.group()}")
    else:
        print(f"{value} 没有匹配到")

# 2. (ab) 分组
#匹配邮箱 163.com qq.com 126.com
print("______________________2. (ab) 分组______________________")
m2 = re.match(r'\w{4,10}@(126|163|qq)\.com',"hello@qq.com")  # \. 是转义字符--匹配.
if m2:
    print(f"m2:{m2.group()}")
else:
    print(f"m2 没有匹配到")






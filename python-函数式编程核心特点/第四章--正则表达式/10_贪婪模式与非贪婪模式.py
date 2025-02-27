# 贪婪模式与非贪婪模式
# 贪婪模式：尽可能多的匹配
# 非贪婪模式：尽可能少的匹配

import re

info = '<div>python</div><div>mysql</div>'

# 贪婪模式
m1=re.match('<div>.*</div>',info)
if m1:
    print(f"m1:{m1.group()}")
else:
    print(f"m1 没有匹配到")

# 非贪婪模式
m2 = re.match('<div>.*?</div>',info)
if m2:
    print(f"m2:{m2.group()}")
else:
    print(f"m2 没有匹配到")

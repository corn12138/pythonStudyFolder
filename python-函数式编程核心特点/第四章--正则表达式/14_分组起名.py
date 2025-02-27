# 分组起名


import re

# 4. (?P<name>) 给分组起名字
# 5. (?P=name) 引用分组的名字
# 需求：<div>python</div> html title span i img h1 h2 h3 h4 h5 h6

m1 = re.match(r'<(?P<name1>[a-z1-6]+)>(.*)</(?P=name1)>','<div>python</div>') # ?P<name1> 给分组起名字
if m1:

    print(f"m1-2:{m1.group(2)}")
    print(f"m1-1:{m1.group(1)}")
    print(f"m1-全:{m1.group()}")
else:
    print(f"m1 没有匹配到")



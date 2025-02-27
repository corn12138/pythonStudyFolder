#分组提取数据与分组编号

import re

# () 分组的使用,取分组数据时,从1开始
# 提取 电话号码
print(f"{'_'*20}","() 分组的使用",f"{'_'*20}")
m1 = re.match(r'(.+):(1\d{4,10})','电话:10086')
if m1:
    print(f"m1:{m1.group()}") #电话:10086
    print(f"m1:{m1.group(1)}") #电话
    print(f"m1:{m1.group(2)}") #10086

else:
    print(f"m1 没有匹配到")




# 3. \num 引用分组--取分组数据
print(f"{'_'*20}","\num 引用分组",f"{'_'*20}")
# 需求：<div>python</div> html title span i img h1 h2 h3 h4 h5 h6

m2 = re.match(r'<[a-z1-6]+>(.*)</[a-z1-6]+>','<div>python</div>')
if m2:
    print(f"m2:{m2.group(1)}")
else:
    print(f"m2 没有匹配到")

m3 = re.match(r'<([a-z1-6]+)>(.*)</\1>','<div>python</div>') # \1 引用第一个分组
if m3:
    print(f"m3-全:{m3.group()}")
    print(f"m3-1:{m3.group(1)}")
    print(f"m3-2:{m3.group(2)}")
else:
    print(f"m3 没有匹配到")







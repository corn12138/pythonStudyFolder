# 字典合并

dict1 = {'a':1}
dict2 = {'b':2}

#旧版本
dict1.update(dict2) #update-是字典的合并
print(dict1)

#新版本 |
res= dict1 | dict2
print(res)

#更新字典
dict1 |= dict2  #等价于 dict1 = dict1 ｜ dict2

print(dict1)


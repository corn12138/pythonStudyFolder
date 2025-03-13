#字典新特性

data = {'a':1,'b':2,'c':3}

print(f'{data = }')

#items values keys

# print(f'items = {data.items()}')
# print(f'values = {data.values()}')
# print(f'keys = {data.keys()}')

#新版本------------------------------
keys = data.keys()
items = data.items()
values = data.values()
# print(f'mapping = {keys.mapping}')
# print(f'mapping = {items.mapping}')
# print(f'mapping = {values.mapping}')

#旧版本
keys = ['name','age','sex']
values = ['Tom',20,'男']
data = dict(zip(keys,values)) #zip函数--将两个列表合并成一个字典
print(f'创建的{data = }')

#新版本------------------------------

data_dict2 = dict(zip(keys,values,strict=True)) #strict=True 严格模式，如果key和value的数量不一致，会报错
print(f'{data_dict2 = }')


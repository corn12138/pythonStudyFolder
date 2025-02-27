#  字符串格式化输出
# 旧版本
name = 'Tom'
age = 20
print('我叫%s,今年%d岁' % (name, age))

# 新版本--format
print('我叫{0},今年{1}岁'.format(name, age))

# 新版本--f-string
print(f'我叫{name},今年{age}岁')
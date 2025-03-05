#  字符串格式化输出

name = 'Tom'
age = 20
names = ['Tom', 'Jerry', 'Spike']
# 旧版本


print('我叫%s,今年%d岁' % (name, age))

# 新版本--format
print('我叫{0},今年{1}岁'.format(name, age))

# 新版本--f-string
print(f'我叫{name},今年{age}岁')
print(f'我叫{names[0]},名称{names[1]},名称{names[2]}')


a = 10
b = 20
# 表达式
print(f'{a}+{b}={a+b}')
print(f"{a}*{b}={a*b}")
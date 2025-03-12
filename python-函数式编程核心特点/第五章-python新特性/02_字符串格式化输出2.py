a = 10
b = 20
print(f'{a = }, {b = }')

# 使用指定字符填充
name = 'baizhan'

# 使用*居中显示
print('{:*^20}'.format(name))
print(f"{name:*^20}")  #

#数值变量的格式化
price = 122.345
print('{:.2f}'.format(price))

print(f'{price:.2f}')

num = 12
print(f'{num:.1f}')

pct =0.789
print('{:.2f}%'.format(pct*100))
print(f'{pct:.2%}')  # 新特性写法
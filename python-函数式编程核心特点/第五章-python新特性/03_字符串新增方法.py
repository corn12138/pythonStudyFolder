# 删除前缀 --  区分大小写
res = 'abcdefg'
print(res.removeprefix('a'))  # bcdefg

# 删除后缀 --  区分大小写
res = 'abcdefg'
print(res.removesuffix('g'))  # abcdef

# 字符串转换为ASCII码
res = 'abc'
print(res.encode())  # b'abc'

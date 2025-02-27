# 迭代器的概念_for循环的本质

# 1.迭代器的概念: 迭代器是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 2.for循环的本质: for循环本质上就是通过不断调用next()函数实现的。
# 3.迭代器的特点: 迭代器只能往前不会后退。迭代器的两个基本方法是iter()和next()。
from collections.abc import Iterable, Iterator

a = isinstance([], Iterable)
b = isinstance([], Iterator)
print(a) # True
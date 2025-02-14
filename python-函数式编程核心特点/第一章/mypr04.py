# 闭包核心概念_内存分析_第一个闭包程序(重要)

#概念：闭包是由函数及其相关引用环境组合而成的实体（即：闭包=函数+引用环境）。闭包是一种特殊的对象，它由两部分组成：函数及其相关的引用环墋。闭包是一种特殊的对象，它由两部分组成：函数及其相关的引用环境。引用环境中包含了这个函数所在的作用域中的所有局部变量。闭包是一种特殊的对象，它由两部分组成：函数及其相关的引用环境。引用环境中包含了这个函数所在的作用域中的所有局部变量。

# 闭包的作用：可以将一些数据隐藏在内部，只暴露一些接口给外部使用，这样可以保护数据不被外部随意修改。
"""
闭包的特点：
1.存在内外层函数嵌套的情况
2.内层函数引用了外层函数的变量或者参数（自由变量）
3.外层函数把内层的这个函数本身当作返回值返回
"""

def outer():
    print("outer")
    a = 1 # 局部变量
    def inner():
        print("inner")
        nonlocal a # 声明外部函数的局部变量--目的是为了修改外部函数的局部变量
        print(f"a:{a}") # 访问外部函数的局部变量,这个局部变量就是闭包的引用环境
    return inner

inn = outer()
print("000000")
inn()

# 闭包的应用场景：1.装饰器 2.回调函数 3.函数式编程
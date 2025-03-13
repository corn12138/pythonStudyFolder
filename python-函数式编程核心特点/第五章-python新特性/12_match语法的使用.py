# match语法的使用
status = 404

match status:
    case 200:
        print("ok")
    case 404:
        print("not found")
    case 500:
        print("error")
    case _:
        print("other")


p1 =('zs',18,'man')
p2 =('ls',20,'woman')
p3 =('ww',21,'male')


def func_test(person):
    match person:
        case (name,_,'man'):
            print(f"{name}是男性")
        case (name,_,'woman'):
            print(f"{name}是女性")
        case (name,age,sex):
            print(f"{name},{age},{sex}")

print(func_test(p1))
print(func_test(p2))
print(func_test(p3))
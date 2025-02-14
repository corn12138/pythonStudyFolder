# sorted排序和自定义对象的排序
# 排序 sorted 排序的逻辑是，先比较第一个元素，然后比较第二个元素，以此类推

sorter = sorted([4,2,1,7,3,2])
print(sorter)

sorter2 = sorted([1,3,6,-20,-70],key = lambda x:abs(x)) # 按照绝对值排序
print(sorter2)

sorter3 = sorted(["ABC","abc","CDE","cde"])  # 按照ASCII码排序
print(sorter3)

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "({},{})".format(self.name,self.age)

s1 = Student("zhangsan",20)
s2 = Student("lisi",18)
s3 = Student("wangwu",22)
s4 = Student("zhaoliu",19)

# sorter4 = sorted([s1,s2,s3,s4],key = lambda x:x.age)
# print(sorter4)

from functools import cmp_to_key #引入cmp_to_key函数
key = cmp_to_key(lambda x,y: x.age - y.age) #定义一个比较函数
sorter5 = sorted([s1,s2,s3,s4],key = key)

print(sorter5)
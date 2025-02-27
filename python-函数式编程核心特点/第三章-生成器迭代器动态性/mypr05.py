# 迭代器_手动创建一个迭代器

class MyNumbers:
    def __iter__(self):
        self.num = 10
        return self
    
    def __next__(self):
        if self.num < 40:
            x = self.num
            self.num += 10
            return x
        else:
            raise StopIteration # 迭代器结束
        
if __name__ == '__main__':
    try:
        myclass = MyNumbers()
        myiter = iter(myclass)
        print(next(myiter))
        print(next(myiter))
        print(next(myiter))
        print(next(myiter))
        print(next(myiter))
        print(next(myiter))
    except StopIteration as e:
        print(e)
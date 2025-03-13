# dataclass装饰器的使用

from dataclasses import dataclass, field
from typing import ClassVar

@dataclass # 使用dataclass装饰器--->他的作用 是自动为类添加__init__方法，__repr__方法，__eq__方法，__hash__方法，__str__方法，__lt__方法，__le__方法，__gt__方法，__ge__方法，__ne__方法，__annotations__方法，__dataclass_fields__方法，__dataclass_params__方法，__post_init__方法，__dataclass_self__方法，__dataclass_class__方法，__dataclass_order。
class Player:
    # 类变量
    name:str
    position:str
    age:int
    sex:str=field(default='male',repr=False) #设置
    # msg:str=field(default="")
    msg:str=field(default_factory=str)
    #类变量
    country:ClassVar[str]



if __name__ == '__main__':
    #创建实例对象
    p = Player('zs','北京',20)
    print(p)
    Player.country = 'china'
    print(Player.country)

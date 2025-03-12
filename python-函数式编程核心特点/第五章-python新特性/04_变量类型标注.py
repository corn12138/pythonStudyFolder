
#简单的变量类型标注
a:int = 10
b:str = 'hello'
c:float = 3.14
d:bool = True
e:bytes = b'hello' # bytes类型,

#复杂的变量类型标注
from typing import List, Tuple, Dict, Any, Union
x:List[int] = [1,2,3] # 列表类型
y:Tuple[int, str, float] = (1, 'hello', 3.14) # 元组类型
z:Dict[str, int] = {'a':1, 'b':2} # 字典类型
m:Union[int, str] = 10 # 可以是int或者str类型
x1:set[int] = {1,2,3} # 集合类型
y1:tuple[int,...] = (1,2,3) 


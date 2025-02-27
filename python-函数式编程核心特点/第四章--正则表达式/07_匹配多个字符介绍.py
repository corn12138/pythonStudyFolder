# 匹配多个字符介绍
    #1. * 匹配前一个字符0次或无限次 ，* 号前面的字符可以出现0次或者无数次，例如：a* 可以匹配0个a，也可以匹配任意多个a
    #2. + 匹配前一个字符1次或无限次 ，+ 号前面的字符可以出现1次或者无数次，例如：a+ 可以匹配1个a，也可以匹配任意多个a
    #3. ? 匹配前一个字符0次或1次 ，? 号前面的字符可以出现0次或者1次，例如：a? 可以匹配0个a，也可以匹配1个a
    #4. {m} 匹配前一个字符m次，{m} 号前面的字符必须出现m次，例如：a{3} 可以匹配3个a
    #5. {m,n} 匹配前一个字符m到n次 ，{m,n} 前面的字符可以出现从m到n次，例如：a{1,3} 可以匹配1到3个a

import re

ret = re.match(r"[A-Z][a-z]*", "M")
print(f"ret:{ret.group()}")  #M

ret = re.match(r"[A-Z][a-z]*", "MnnM")
print(f"ret:{ret.group()}")  #Mnn
ret = re.match(r"[A-Z][a-z]*", "Abcdef")

print(f"ret:{ret.group()}")  #Abcdef


match_obj = re.match(r"t[0-9]+", "t123t")
print(f"match_obj:{match_obj.group()}")  #t123

match_obj1 = re.match(r"https?", "http")
print(f"match_obj1:{match_obj1.group()}")  #http

match_obj2 = re.match(r"[a-zA-Z0-9]{6}", "12a3g45678")
print(f"match_obj2:{match_obj2.group()}")  #12a3g4

match_obj3 = re.match(r"[a-zA-Z0-9]{6,20}", "12a3g4567809HighGUI")
print(f"match_obj3:{match_obj3.group()}")  #12a3g45678


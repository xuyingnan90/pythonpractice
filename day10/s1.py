#!/user/bin/env python
# -*- coding:utf-8 -*-

i = 0
while i < 3:
    print("Ha %s" % (i))
    i = i + 1

'''
运算符
+ - * / 

%

** --------返回x的y次幂  x**y

//---------取整除，返回商的整数部分


in ——————————在
not in ——————不在

"四级啊" 字符串 "级啊" 是其子序列


布尔值 true false
 ==
 > 
 < 
 >= 
 <= 
 != 不等于
 <> 不等于
 not
 and
 
 优先级计算
 先计算括号内
 执行顺序 ：
    从前到后
    结果 true or ----->true
        true and ------继续走
        false or ------继续走
        false and -----false
 
 
 c=c+1    ----- c+=1
 
 结果是值：
    算术运算
 
    赋值运算
 
 
 ------------
 结果是布尔值：
 
    比较运算
 
    逻辑运算
 
    成员运算（in  ,  not in）
    
---------------    
---------------
    

'''
name="四级啊"
v="四啊" not in name
a=123
s=a.bit_length()
print(s)
if v:
    print("not in")
else:
    print("in")




# 递归 问路
# 迭代 可被for循环

# 迭代器协议：对象必须提供一个next（）方法，执行该方法要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代（只能往后走不能往前退）
# 可迭代对象：实现了迭代器协议的对象
l = [1, 2, 3]
for i in l:  # 先执行__iter__()，把列表变成可迭代对象 遵循迭代器协议
    pass

k = l.__iter__()
print(k.__next__())
print(k.__next__())
print(k.__next__())


l=["a","b","c","d"]
asd=l.__iter__()
print(next(asd))


#生成器 可以理解为一种数据类型 自动实现了迭代器协议 所以生成器就是可迭代对象

#1.生成器函数
# yield
def test():
    yield  1
    yield  2
    yield  3

g=test()
print(g.__next__())
print(g.__next__())
print(g.__next__())


#2.生成器表达式
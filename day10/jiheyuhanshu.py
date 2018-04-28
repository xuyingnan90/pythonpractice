# -*- coding:utf-8 -*-

'''
数据类型和变量总结

变量
    用来记录状态
    处理状态变化


可变：列表 字典


不可变：字符串 数字 元组


访问顺序
    1.顺序访问：字符串 列表 元组
    2.映射：字典（访问速度比列表元组快 但占内存也高）
    3.直接访问：数字

存放元素个数

    容器类型

        列表 元组 字典

    原子类型

        数字 字符串

集合：
    由不同元素组成的集合，集合中是一组无序排列的可hash值，可以作为字典的key

集合的三个要素

    * 不同元素组成
   ** 无序
  *** 只能存放数字/字符串/元组（不可变类型）

'''

# s = {"Hello", "World", "Roddick", "Alex", ("w", "s")}
# for i in s:
#     print(i)
#
# print(s)

# li = ("a", "b", "c")
# li = {
#     "k1": "v1",
#     "k2": "v2"
# }
# v = set(li)  # set()定义可变集合   (如果只想做简单的去重而不需要考虑原来的模样 用SET（）就可以)
# print(v)

# 添加 add()

# s = {"ssd", 1, 2, 3, 4, 5, 6, 7, "s"}
# s.add(("ss", "ddd"))
#只能添加一个参数
# print(s)

# clear() 清空
# s.clear()
# print(s, "sss")
set

# pop() 随机删除

# s.pop()

# remove()指定删除  如果删除的元素不存在 会报错
# s.remove("ssd")

# discard()删除的元素不存在也不会报错
# s.discard("ssdssss")

p1 = ["pn1", "pn2", "pn3", "pl1", "pl2"]
l1 = ["ln1", "ln2", "ln3", "pl1", "pl2"]
#
se1 = set(p1)
se2 = set(l1)
# 求交集
# se12=se1.intersection(se2)
# se12 = se1 & se2
# 求并集
# se13=se1|se2
# se13 = se1.union(se2)
# 求差集 a-b  求a中有 b中没有的元素
# se14 = se1 - se2
# se14 = se1.difference(se2)
# print("", se1, "\n", se2, '\n', se12, '\n', se13, '\n', se14)

#交叉补集
#s15=se1^se2
# s15=se1.symmetric_difference(se2)
# print("",s15)


# difference_update() 做差集并更新集合
#se1-se2 不会更新se1  但difference_update()会更新se1
# v=se1.difference_update(se2)
# print(se1)

#isdisjoint() 判断是否有交集部分  没有交集会返回True
# v=se1.isdisjoint(se2)
# print(v)

#issubset() 包含 a.issubset(b) a是否是b的子集
# ls1={1,2,3}
# ls2={1,2}
# v=ls2.issubset(ls1)
# print(v)

#issuperset() a.issuperset(b)  a是否是b的父集
# ls1={1,2,3}
# ls2={1,2}
# v=ls1.issuperset(ls2)
# print(v)


#update()  a.update(b)  等同于 做ab并集并赋给a  b为可迭代元素 可更新多个值 相比于add()更强大
# a={1,2,3,4}
# b={1,2,5,6,7}
# a.update(b)

# print(a)


#frozenset() 定义不可变集合没有add() update() 等方法
frozenset

# pls=["as","dk","dk",12,44]
# plse=frozenset(pls)
# v=plse.symmetric_difference(p1)
# print(v)
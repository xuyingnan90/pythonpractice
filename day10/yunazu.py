'''
元组 tuple
元组是可迭代对象 字符串  列表 也是可迭代对象
元组不可被修改，增加，删除
元组有序
1.书写 tu=(1,2,3,4,)
一般写元组的时候，在最后变加个逗号
2.索引
可通过索引访问
3.切片
4.元组是可迭代对象 字符串  列表 也是可迭代对象 可以被for循环
5.与字符串 列表之间的转换
6.元组的一级元素不可更改/删除/增加 但元组中的列表内的元素可以更改
'''

tu = (111, "as", (212, "asd"),[2,3,4])
#
# v=len(tu)
# print(v)

# strs = "jasdasdas"
# v = tuple(strs)
# print(v)

# tu[3][0]=[22,33,44] #元组的一级元素不可更改/删除/增加 但元组中的列表内的元素可以更改

v=tu.index(111)
# v=tu.count(111)

print(v)


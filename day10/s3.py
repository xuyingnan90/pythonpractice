'''
list 列表
列表元素可被修改
列表 是一个集合，内部可以放置任何东西
列表是有序的 元素可以被修改

1.列表的基本格式
2.列表嵌套的类型
3.列表索引
4.列表切片
5.for 循环
6.while 循环
7.通过索引取值
8.通过切片取值

'''

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ["Alex", "Roddick"]]

'''
以下为索引方式
'''
# li[3]=33
# del li[3]
'''
以下为切片方式
'''

li[3:5] = [33, 44]
# del li[3:5]
print(li)


v=["Alex", "Roddick"] in li
print(v)

#将字符串转换为列表
# st="askdadkj"
#
#
#
#
# newli=list(st)
#
#
# print(newli)
#列表与字符串转换
lii=['a', 's', 'k', 'd', 'a', 'd', 'k', 'j']

s=""
for i in lii:
    s+=str(i)

print(s)


#如果列表内部只有字符串 则可以使用字符串的join方法
# y=["123","co"]
# vs="".join(y)
# print(vs)


#列表的方法
#append()  在最后追加
# li=[1,2,3,4]
# li.append(["12s","sss"])
# print(li)

#clear()  清空列表
#
# li.clear()
# print(li)


#copy 复制 浅拷贝
#
# kl=li.copy()
# print(kl)

#count 计算元素出现的次数

# n=li.count(33)
# print(n)

#extend() 扩展原来列表 参数为可迭代对象

# li.extend([9898,"不得了"])
# li.extend("不得了")

# li.append([9898,"不得了"])
# print(li)


#index(value,start=none,end=none) 返回参数首次出现的位置

# list1=[1,2,3,4,5,6,7,7,7,7,8,9,0]
# vb=list1.index(7,7,9)
# print(vb)

#insert() 在指定位置插值
list2=[0,1,2,3,4,5,6,7,8,9]
list2.insert(0,"A")
print(list2)

#pop() 删除指定位置的元素 默认为最后一个
# list3=[1,2,3]
# v3=list3.pop(0)
# print(list3,v3)

#remove() 删除列表中的指定值 左边优先
# list4=[1,2,3,4,2]
# list4.remove(2)
# print(list4)


#列表的删除
#pop()         remove()         del li[x]       del li[x:x+2]       clear()


#reverse() 反转
#
# list5=[1,2,5,"asd",4]
# list5.reverse()
# print(list5)

# list6=[11,113,12,22,33,44]
# list6.sort(reverse=True)
# print(list6)



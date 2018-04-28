'''
整理

    数字:
        int()

    字符串:
        replace() find()  join() strip() startwith() split() upper() lower() format()

    列表:
        append() extend() insert()
        索引 切片 循环...

    元组:
        了解
        索引 切片 循环...
        一级元素不能被增删改

    字典:
        get() update() keys() values() items()
        for循环 索引

    布尔值:
        bool()
        在内存中以0,1存储
        None "" {} () [] 0==>False(js中 {}，[]是真)

'''

# -------------------------------------------------
# 字符串 format()
# t=" i am {name},age: {age}"
#
# # v=t.format(name="Alex",age=20)
# v= t.format(**{"name":"Alex","age":20})
# print(v)
# -------------------------------------------------


# -------------------------------------------------
# 字典
# dic = {
#     "k1": "v1",
#     "k2": "v2"
# }
#
# v = "k1" in dic.keys()
# print(v)
# -------------------------------------------------


# l1=[11,22,33]
# l2=[22,33,44]
# d=[]
# s=[]
# for i in l1:
#     if i not in l2:
#         d.append(i)
#
# for i in l2:
#     if i not in l1:
#         s.append(i)
#
#
# d.extend(s)
# print(d,s)
# c = 0
# arr = [3,4,5,6]
# for i in arr:
#     for v in arr:
#         if i != v:
#             c += 1
# print(c)

arr = range(1, 10)
for i in arr:
    str1 = ""
    for j in range(1, i + 1):
        #print("%s * %s= %s" % (i, j, i * j))
        str1+=str(j)+"*"+str(i)+"="+str(i*j)+"\t"

    print(str1)
    str1=""
print("-"*50)





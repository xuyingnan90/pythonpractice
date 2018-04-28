'''
函数式编程（实现简单，但易读性差）
    高阶函数
        1.不可变
            不用变量保存状态，不修改变量
        2.函数即变量
            高阶函数（至少包括一下一个条件）
                1.把函数名当做参数传给另外一个函数
                2.返回值中包含函数
            高阶函数作用
        3.尾调用优化
            在函数的最后一步调用另外一个函数（最后一步不一定是函数的最后一行）

    map函数
        map(方法，可迭代对象)

        filter(方法，可迭代对象)
'''

from functools import reduce

# def foo(n):
#     print(n)
#
# def bar(name):
#     print("Hello %s"%(name))
#     return foo

# print(foo(bar("Moto")))

# def foo():
#     print("from foo")
#     return bar
#
#
# def bar():
#     print("from bar")
#
#
# n = foo()
# n()

# def es():
#     print("from es")
# def h():
#     print("from h")
#     return es()
#
# n=h()

# num_1 = [1, 2, 3, 4, 5, 6, 7]
# num_2 = []
#
#
# def add_num(x):
#     return x + 1
#
#
# def reduce_num(x):
#     return x - 1
#
#
# def el_num(x):
#     return x ** 2
#
#
# def map_list(fun, arr):
#     l = []
#     for i in arr:
#         res = fun(i)
#         l.append(res)
#     return l


# ls=map_list(lambda x:x**2,num_1)
# ls=map_list(reduce_num,num_1)
# ls = map(lambda x: x ** 2, num_1)
# print(ls)
# for i in ls:
#     print(i)

# print(list(ls))

#
# msg = "jjsjjhdfka"
# print("".join(list(map(lambda x: x.upper(), msg))))
msg = ["lksss", "slll", "skdjksd", "ddddd", "qweqq"]

# def fil_arr(fun,arr):
#     rs = []
#     for i in arr:
#         if not fun(i):
#             rs.append(i)
#
#     return rs
#
#
# # k = fil_arr(lambda x:x.startswith("l"),msg)
# # k=list(filter(lambda x:not x.startswith("l"),msg))
#
# k=list(map(lambda x:x.upper(),msg))

num_l = [1, 2, 3, 100]


# sums=0
# for i in num_l:
#     sums+=i
# print(sums)
# def fun1(a, b):
#     return a * b
#
#
# def reduce_num(fun, arr,init=None):
#     if init is None:
#         a=arr.pop(0)
#     else:
#         a=init
#     # a = arr.pop(0)
#     for i in arr:
#         a = fun(a, i)
#     return a
#
#
# k = reduce_num(fun1, num_l,100)
# print(k)

k=map(lambda x:x*2,num_l)
arr=list(k)
m=reduce(lambda x,y:x+y,arr,1)
print(arr,m)






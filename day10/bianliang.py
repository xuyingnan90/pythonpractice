'''
全局变量
'''

'''
在子程序里定义的 有缩进的变量 是局部变量
'''

# def fun1():
#     name = "x1"
#     print(name)
#
#     def fun2():
#         # name="x2"
#         print("x2")
#
#         def fun3():
#             # name="fun3"
#             print("x3")
#
#         fun3()
#
#     fun2()
#
#     print(name, 1)
#
#
# fun1()

#

# name = "刚娘"
#
#
# def weihou():
#     name = "沉着"
#     ld="sdds"
#     def weiweihou():
#         global name
#         name = "冷静"
#         ld="s"
#         def wei():
#             nonlocal ld
#             ld = "lk"
#             # print(name, 4)
#
#             print(ld, 4)
#
#         wei()
#
#     print(ld)
#     weiweihou()
#
#     print(name, 3)
#
#
# print(name, 1)
# weihou()
# print(name, 2)

'''
结果：

    刚娘 1
    沉着 3
    冷静 2


'''

'''
nonlocal name 指代上一级变量
'''


'''
前向引用

'''

def foo():
    print("from foo()")
    bar()

def bar():
    print("from bar()")

foo()

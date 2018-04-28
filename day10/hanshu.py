# 函数
# 为了完成某功能

# def function_name(x):
#     "此处为注释"
#     y=2*x+1
#     return y
#
# print(function_name(3))

# 过程
# 就是没有返回值的函数，实际PYTHON会给没有返回值的函数返回None
'''
没设置返回值 会返回None
返回值数=1  返回object
返回值数》1 返回tuple

'''


def test1():
    s = "HOOOO"
    print(s)


def test2():
    s = "ddddd"
    print(s)
    return 2, [1, 2, 3, 4, 5]


v1 = test1()
v2 = test2()
print(v1)
print(v2)

'''
形参：不占内存空间



实参：占内存空间

位置参数：必须一一对应  test(1,3,2)
关键字参数：位置无需固定 test(x=1,z=2,y=3)
位置参数与关键字参数混用 一定要在关键字参数左边
默认参数 test(1,2,type="xxx.txt")
参数组  def test(x,*args)


'''

'''
def test(x, *args):
    print(x)
    print(args)


test(1, *[2, 3, 4, 5, 6])  # (2, 3, 4, 5, 6)
# test(1,[2,3,4,5,6]) #([2, 3, 4, 5, 6],)

'''


def test(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)


test(1, 1, 2, 3, 4, 5, 6, **{"a": "Alex", "z": 1})

'''
*args 要在 **kwargs之前
'''

# abs() 取绝对值
# k=abs(-5.5)
# print(k)

# all()取布尔值 一假必假
# k=all([1,2,3,"das",-1,0])#返回True
# k=all("0")#返回True
# k = all({1, 2, 0})  # 返回False
# print(k)

# any()取布尔值 一真必真
# k=any([0,1])
# print(k)

# bin()十进制转二进制
# k=bin(3) #返回0b11
# print(k)

# bool() 转布尔值（空 None 0 布尔值为false）
# k=bool(None)
# print(k)

# bytes()字符串转字节
# k = "你好"
# print(bytes(k, encoding="utf-8").decode("utf-8"))

# chr() 编码转字符 ord()字符转编码

# print(ord("中"))
# print(chr(20013))


# dir()打印某一个对象下 有哪些方法 属性

# divmod()
# print(divmod(10,3))#返回（3,1）商3余1 可用于分页

# seq = ['one', 'two', 'three']
# print(list(enumerate(seq, start=1)))

# eval() 1.提取字符串中的数据结构 2.把字符串中的表达式进行运算

# k="1+2*3"
# print(eval(k))


# hash() 可哈希的数据类型即不可变数据类型 不可哈希的数据类型即可变数据类型 可用于下载文件校验
# str="sadadada"
# s="sadadada"
# print(hash(s),hash(str))

# help()查看帮助

# hex() 十进制转十六进制
# oct()十进制转八进制

# isinstance() 判断数据类型
# k=isinstance("1",str)
# print(k)#True


# globals() 打印全局变量 包括系统预定的以及自己设定的
# names="sd"
# print(globals())
# print(__file__)

# locals()打印当前作用域的变量
#
# def test():
#     name="sadasd"
#     print(locals())
# test()

# max()取最大值 如果比较的是字典 则默认比较的是字典的key 不同类型间不能进行比较 字符串和数字 参数为可迭代类型

# age_dic={"age11212121":18,"age3":20,"age4":10}
# k=zip(age_dic.values(),age_dic.keys())
# print(list(max(k)))
# print(max(age_dic.values()))
# l = [
#     (5, "e1"),
#     (4, "e2"),
#     (3, "e3"),
#     (33, "e4"),
#     (1, "e5"),
# ]
# s=["a10","b12","c10"]
# print(max(s))
# print(list(max(l)))

# p = [
#     {"name": "Alex", "age": 18},
#     {"name": "Roddick", "age": 100},
#     {"name": "Sum", "age": 288},
# ]
# print(max(p,key=lambda x:x.get("age")))

# min()取最小值

# zip()   zip函数接受任意多个可迭代对象作为参数,将对象中对应的元素打包成一个tuple,然后返回一个可迭代的zip对象.

# k=[1,2,3,4]
# l=["a","b","c","d"]
# s=["aa","bb","cc"]
# # o=list(zip(l,k,s))
# o=list(zip([1,2],"121i3sd"))
# print(o)

# p={"name":"Alex","age":18,"gender":"M"}
# print(list(zip(p.keys(),p.values())))


# pow(n,e) n**e
# pow(n,e,m) n**e%m

# reversed() 反转

# st = [1, "sda", 2, 4, 3, "dsad"]
# s = reversed(st)
# print(st) #[1, "sda", 2, 4, 3, "dsad"]
# print(list(s)) #['dsad', 3, 4, 2, 'sda', 1]


# round()四舍五入

# slice() 切片
# p = [0, 1, 2, 3, 4, 5, 6, 7]
# s = slice(3, 5)
# print(p[s])


# l="dsfshdfjgklhkj;"
# s=slice(1,8,2)
# print(l[s])

# sorted() 本质是比较大小 不同类型不能比较大小
# p = [
#     {"name": "Roddick", "age": 100},
#     {"name": "Alex", "age": 18},
#
#     {"name": "Sum", "age": 288},
# ]
#
# l = sorted(p, key=lambda x: x.get("age"),reverse=True)
# p = {
#     "ayuanhao": "2018-11-20",
#     "alex": "2017-01-02",
#     "wupei": "2018-11-12",
#
# }
# l = sorted(zip(p.values(), p.keys()), reverse=True)
# # l=sorted(p,key=lambda key:p.get(key),reverse=True)
# print(l)

# p="{'name':'Alex','age':20}"
# print(type(eval(p)))

# sum()求和

# l=[1,2,3,4]
# print(sum(range(2,5)),list(range(2,5)))

# type()
# msg="123"
# if type(msg) is str:
#     print("str")

# vars() vars() 函数返回对象object的属性和属性值的字典对象。如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。
# def test():
#     m="a"
#     print(locals(),vars())
#
# test()


# import 不能导入字符串文件名  需要用__import__(name)

# import test
#
# test.say_hi()

# modules_name="test"
# m=__import__(modules_name)
# m.say_hi()

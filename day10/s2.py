'''
数字      int
字符串    str
列表      list
元组     tuple
字典     dict
布尔值    bool


'''

# 数字 int
# python3里， 所有的整型都是int类型

# int
s = "abcd"
a = 4

# 数字
'''
- int
    将字符串转换为数字
    int（num,base=2） 将num按照2进制转换 成十进制
    
    2
'''
# str
print(type(s), type(a))

r = a.bit_length()
# bit_length()当前数字的二进制至少用多少位表示
print(r)

test = "aLasdfadasfgv"
v=test.find("a",5,8)
print(v)
# v=test.capitalize() 首字母大写
# v=test.casefold() 将字符串转为小写 功能比lower（）强大
# v=test.lower() 将字符串转为小写
# v=test.center(20,"中") 将一个在宽度为20的容器里的字符串居中
# v=test.count("LE"，5,6) 统计某个字符或子序列出现的次数，在5~6位置之间
# v=test.endswith("a")   字符串是否以"a"结尾
# v=test.startswith("a") 字符串是否以"a"开头
# v=test.find("a"，5,8) 从前往后寻找某字符或子序列首次出现的位置（在第5~8（不包括第八位）位之间）
# te="i am {name},age {age}"
# v=te.format(name="Alex",age=19)  te.format_map({name:"Alex",age:19})
# v=test.index('Ex') 如果找不到会直接报错 建议使用 find（）
# te="sd1111"
# v=te.isalnum() 判断字符串中是否只是数字字母
# s="gfuigfsdgkjsffgh\tjkhjsdgfskyfg\thjksdhfjksh"
# v=s.expandtabs(6)
# v=test.isalpha() 是否是字母汉字
# te="②"
# v1=te.isdecimal()
# v2=te.isdigit()
# v3=te.isnumeric()
# print(v1,v2,v3)
# te="test\tsjaij" 是否存在不可见的字符 \t    \n
# te="sadfaafasfadf"
# v=te.isprintable()
# te="sdfsfs     "
# v=te.isspace() 判断是否全部由空格组成
# te="Return true if all cased"
# v=te.title() 将字符串转换为标题格式
# v=te.istitle() 判断字符串是否为标题格式
# te="前端高能"
# ds=" ".join(te) #将字符串中的每一个元素按照指定分隔符进行拼接
# print(ds)
# te="alAex"
# v=te.ljust(20,"*")
# v=te.islower()


# v=te.rjust(20,"*")

# v1=te.isupper() 判断是否全部为大写
# v2=te.upper()  全部转为大写

# print(v1,v2)


# te="一人，我，饮酒，醉"
# vi=te.split("，",2)
# print(vi)
# v=te.lstrip() 去掉左侧空格 以及\t \n 前缀字符
# v=te.rstrip() 去掉右侧空格
# vs=te.strip("k") #去掉左右空格
# print(vs)
# v=te.rstrip("ex ")


# te="gjhagsdj dhsajkdkasjdd akd kdhaskjdh jkasd kah kjhkjashdkjhk"
# m=te.maketrans("kad","尅诶第")
# v=te.translate(m)


# print(v)

# formatstr="i am {name},age {age}"
# v1=formatstr.format(name="Alex",age=20)
# print(v1)


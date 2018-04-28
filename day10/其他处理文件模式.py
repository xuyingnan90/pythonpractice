# r+ 即能读又能写
#
# f=open("verse.txt","r",encoding="GBK")
# data=f.readlines()
# f.close()
# # for i,e in enumerate(data):
# #     print(i,data[i])
#
# f1=open("nn","w",encoding="gbk")
# f1.write(data[0])
# f1.close()


# with open("verse.txt", "r", encoding="gbk") as f1, open("newfile", "w", encoding="gbk"):  # 文件以什么编码存的 就以什么编码打开
#
#     data = f1.readlines()
#     for i, e in enumerate(data):
#         print(i, data[i])
'''
r   只能读

r+  可读可写，不会创建不存在的文件。如果直接写文件，则从顶部开始写，覆盖之前此位置的内容，如果先读后写，则会在文件最后追加内容。

w+  可读可写 如果文件存在 则覆盖整个文件 不存在则创建

w   只能写 覆盖整个文件 不存在则创建

a   只能写 从文件底部添加内容 不存在则创建

a+  可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建

'''
# with open("open模式", "r+", encoding="gbk") as f:
#     # d=f.readline()
#     d=f.readline()
#     # print(d)
#     f.write("茫茫啊啊啊人海的得到的是对吖啊啊大大")


# with open("open模式","rb") as f:
#     # print(f.read())
#     data=f.read()
#     print(data)
#     #字符串-->encode-->bytes
#     #bytes-->decode-->字符串
#     k=data.decode("gbk")
#     print(k)


# with open("kio", "r+", encoding="gbk",newline="") as f:  # windows 平台的回车是“\r\n” python默认会把回车同一换成“\n” ,newline=""表示不需要python的默认转换
#     # f.write("sd是\nsadsadasd大萨达所".encode("gbk"))
#     # print(f.encoding)
#
#     print(f.tell())
#     # print(f.read()) read()中参数表示读取的字符数，注意 是字符数！
#     # print(f.readlines())
#
#     print(f.readline())
#     # print(next(f))
#     # print(f.name)
#     print(f.tell())  # tell()返回光标位置 换行--》“\n\r” 占两个字节
#     f.seek(1)#设置光标位置
#     print(f.tell())
#     print(f.readlines())
#     # print(f.tell())
#     # f.write("11111\n")
#     # f.truncate(10) #truncate()为写操作 除了r,W+


'''
seek()补充
'''
# seek() 三个参数 第一个：字节数  第二个：0,1,2  0是绝对 1是相对（相对上一次光标位置）如果设置为1 则要以b模式打开 2相对位置 倒序 此时第一个参数应为负数 也为b模式打开
# b模式 open（）不要有encoding参数
# with open("kio", "rb") as f:
#     print(f.tell())
#     f.seek(-11, 2)
#     print(f.read())

# 读取文件最后一行
# with open("kio", "rb") as f:
#     for i in f:
#         offs = -30
#         while True:
#             f.seek(offs, 2)
#             data = f.readlines()
#             if len(data) > 1:
#                 print("文件的最后一行：%s" % (data[-1].decode("gbk")))
#                 break
#             offs *= 2


with open("文件日志", "rb") as f:
    for i in f:  # 读取文件的每一行，相比于 for i in f.readlines()  更加的高效，因为readlines()是读取全部的内容存于内存，而 for i in f 的方法只是循环一条 取一条 并不是全部存于内存
        offs = -50  # 估算偏移量，即每一行大概的字节数
        f.seek(offs, 2)  # 将光标定位到倒数offs字节位置
        data = f.readlines()  # 从光标处往后读文件，并放在一个列表里
        while True:
            if len(data) > 1:  # 判断列表的长度，如果长度大于1，表示已经读完了最后一行，并且读到了倒数第二行的内容
                print("最后一条记录为：%s" % (data[-1].decode("utf-8")))
                break
            offs *= 2  # 否则加大偏移量继续循环判断

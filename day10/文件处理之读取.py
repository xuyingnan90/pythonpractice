# open() 打开文件 会检索当前系统的编码
# 操作文件的流程：
# 1. 打开文件，得到文件句柄并赋值给一个变量
# 2. 通过句柄对文件进行操作
# 3. 关闭文件
f = open("sjjj", 'r', encoding="utf-8")
data = f.read() #f.read()表示已经读完全文，如果此时在进行readline（）操作， 无法再读取单行  可以理解为 f.read()之后，光标已经移动到全文的末尾了
# print(data)

# readable() 文件是否可读
print(f.readable())

# # readline() 一次读一行 超出全文的行数后 会读取 空
# print("第1行", f.readline(), end="")
# print("第2行", f.readline(), end="")
# print("第3行", f.readline(), end="")
# print("第4行", f.readline(), end="")
# print("第5行", f.readline(), end="")
# print("第6行", f.readline(), end="")
# print("第7行", f.readline(), end="")
# print("第8行", f.readline(), end="")
# print("第9行", f.readline(), end="")
# print("第10行", f.readline(), end="")
# print("第11行", f.readline(), end="")

# data=f.readlines() #将每一行读取的内容装在列表里
print(data)
f.close()

# 只读 只写 追加

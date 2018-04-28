f = open("sjjj", 'w', encoding="utf-8")
print(f.writable())
# f.read()#在只写模式 会报错
f.write('11111111\n')
f.write('22222222\n')
f.writelines(['sss\n','666s\n'])#文件内容只能是字符串 writelines()参数为列表
f.close()
# msg = "my name is %s , I am %s " % ("Alex", 26)
#
# print(msg)

# 截取字符串 截取三位字符
# tpl="Haa  %.3s"%("sdafafasasf")
# print(tpl)


# 打印浮点数
# tpl="percent %.2f%%"%(99.455555555)
# print(tpl)


# 键值对拼接字符串
# \033[33;1m 开始 更换颜色  （[33;中的33表示颜色对应的序号）
# \033[0m结束
#- 左对齐
#+ 右对齐
# tpl = "I am \033[33;1m%(name)-20s\033[0m ,age %(age).2f " % {"name": "Alex", "age": 18.2566662222}
# print(tpl)


#分隔符
# ms="AVSD".lower()
# v=":".join(ms)
# print(v)
# print("a","v","s","d",sep=":")




#format格式化

# tpl="sjj  jksak{0[1]}  sdajkhklasdhs{1}   dhkladlkasdl{0[2]}".format([1,2,3,4],12,[22,33,44])
# print(tpl)

# tpl="asjd dnsaj dakd{name} akldjkla{age:.2f}".format(**{"name":"Alex","age":19.5666666})
# print(tpl)
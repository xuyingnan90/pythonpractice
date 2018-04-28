'''

字典（类似js中的对象）
info={
"k1":"v1",
"k2":"v2"
}
value可以是任意值
列表不可以作为key 但元组可以
字典不可以做KEY
布尔值可以作为KEY，但key里不能有1或0
python3.6中 字典有序  之前版本字典无序


***比较常用的方法：keys()  values()  items()  get()  update()
'''

info = {
    "k1": 18,
    2: True,
    1: 333,
    True: 12,
    "k3": [
        11, [], (), 22, 33, {
            "kk1": "vv1",
            "kk2": "vv2",
            "kk3": (11, 22)
        }
    ]
    , "k4": (11, 22, 33, 44),
}
# 删除操作
# v=info.pop("k1")
# del info["k3"][5]["kk1"]
# v=info["k3"][5].pop("kk1")

# for i in info:
#     print("%s的值为%s" % (i, info[i]))
# for循环操作
# for k, v in info.items():
#     print(k, v)

# print(info)

# dict

# dict的 fromkeys方法
# 根据第一个参数序列创建字典并赋予统一的值

#
# v=dict.fromkeys(["q","v","o"],10)
# print(v)#结果为：{'q': 10, 'v': 10, 'o': 10}

# get() 根据key获取值，key不存在时可以指定默认值 （默认为None）

# v=info.get("k1","如果该值不存在，则显示此句话")
# print(v)
# pop()
# v=info.pop("k42","如果所删除的key不存在，则显示此话")
# print(info,v)

# popitem() 删除
# dic={
#     "k1":"kkkk1",
#     "k2":"kkkk2"
# }
# v=dic.popitem()
# print(dic,"----"*2,v)


# setdefault(a,b) 设置值  如果a在字典中存在，则返回a的值不设置新值， 如果a在字典中不存在，则返回654
# dic={
#     "k1":"kkkk1",
#     "k2":"kkkk2"
# }
#
# v=dic.setdefault("k12",654)
# print(dic,"-"*8,v)#{'k1': 'kkkk1', 'k2': 'kkkk2', 'k12': 654} -------- 654


# update() 更新

# dic = {
#     "k1": "kkkk1",
#     "k2": "kkkk2"
# }
#
info.update({"k1":654,"k3":789})
# dic.update(k1=654, k3=789, k4=545)
# # 结果{'k1': 654, 'k2': 'kkkk2', 'k3': 789, 'k4': 545}
print(info)
dict
for i in range(1,10):
    s=""
    for j in range(1,i+1):
        s+=str(j)+"*"+str(i)+"="+str(j*i)
        print()
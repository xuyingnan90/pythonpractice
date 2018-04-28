'''
map() 处理序列中的每个元素
filter() 过滤

'''

people = [
    {"name": "Alex", "age": 1000},
    {"name": "ww", "age": 10000},
    {"name": "aaaa", "age": 9000},
    {"name": "x", "age": 20},

]

k = filter(lambda x: x.get("age") < 9000, people)
print(list(k))

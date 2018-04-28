'''
递归

特性
    1.有明确的结束条件，否则会死循环
    2.每次进入更深一层递归，问题规模相比上次递归应有所减少
    3.递归效率不高,递归层次过多会导致栈溢出

'''
import time

# def calc(n):
#     print(n)
#     if int(n / 2) == 0:
#         return n
#     res = calc(int(n / 2))
#     return res
# n=calc(10)
# print(n)


person_list = ["a", "b", "c", "d", "e"]


def askl_way(list):
    print("-" * 60)
    if len(person_list) == 0:
        return "没人知道"
    person = person_list.pop(0)
    if person == "d":
        return "小%s说：我知道，就在那边" % (person)

    print("hi 小%s,你知道xxx在哪吗" % (person))
    print("%s 回答：不知道啊，我帮你问问%s" % (person, person_list))

    time.sleep(2)

    res = askl_way(person_list)
    print("%s问的结果是：%s" % (person, res))

    return res


res = askl_way(person_list)
print(res)

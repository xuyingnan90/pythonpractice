'''
作用域

'''
def test1():
    print("test1")
    return 1

def test2():
    print("test2")
    return test1

res=test2()
print(res())

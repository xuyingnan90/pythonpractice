from functools import reduce

l = [1, 2, 3, 4, 5, 6]
arr = ["sksdf_sb", "namssd", "d_sb_s", "jhsdjkfasfhs", "zncbmzx"]
k = map(str, l)
print(list(k))

m = reduce(lambda x, y: x * y, l)
print(m)

n = filter(lambda x: x > 2, l)
print(list(n))


def findsb(x):
    if x.find("sb") < 0:
        return True


nm = filter(findsb, arr)
print(list(nm))


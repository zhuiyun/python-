# a=lambda a,b:a+b
# print(a(2,3))
# b=lambda :True
# print(b())
# c=lambda x,y=5:x*y
# print(c(2,8))
from functools import partial


def mod(n, m):
    return n % m


mod_by_100 = partial(mod, 100)
print(mod(100, 7))
print(mod_by_100(3))

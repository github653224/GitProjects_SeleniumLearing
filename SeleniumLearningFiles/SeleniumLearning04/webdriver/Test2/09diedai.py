#对元祖、列表或者字符串通过for循环进行遍历叫迭代，在Python中，迭代是通过for ... in来完成的因为Python的for循环不仅可以用在list或tuple上
# ，还可以作用在其他可迭代对象上。 list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无
# 下标，都可以迭代，比如dict就可以迭代：
d={"a":1,"b":2,"c":3}
for key in d:  #或者 for key in d.keys():
    print(key)
print("0===================================================0")
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，
# 可以用for k, v in d.items()。 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for value in d.values():
    print(value)
print("1===================================================1")


for key,value in  d.items():
    print(key,value)
print("2===================================================2")

for i in "ABCD":
     print(i)

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, key in enumerate(["A","B","C"]):
    print(i,key)



























































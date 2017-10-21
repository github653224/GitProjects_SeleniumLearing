#因此，列表生成式也可以使用两个变量来生成list：
d = {'x': "1", 'y': "2", 'z': "3" }
c=[k + "=" + v for k,v in d.items()]
print(c)

# 最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
n = [s.lower() for s in L]
print(n)






























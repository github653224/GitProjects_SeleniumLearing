# Python内建了map()和reduce()函数。
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
     return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个
# 序列都计算出来并返回一个list。
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下
# 一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add(x, y):
    return x + y
pr=reduce(add, [1, 3, 5, 7, 9])
print(pr)















































































































































































# Python内建的filter()函数用于过滤序列。 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数
# 依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1

m=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(m)
# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数

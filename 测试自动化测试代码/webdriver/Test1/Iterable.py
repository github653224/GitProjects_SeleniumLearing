from collections import Iterable
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 可以使用isinstance()判断一个对象是否是Iterable对象：
print(isinstance([],Iterable))

# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并
# 返回下一个值，直到最后抛出StopIteration错误表示无法继续返回
# 下一个值了。可以被next()函数调用并不断返回下一个值的对象称
# 为迭代器：Iterator。可以使用isinstance()判断一个对象是否是Iterator对象
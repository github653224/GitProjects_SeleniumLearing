a=[x*x for x in range(11)]
print(a)

# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，
# 称为生成器：generator。 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个
# 列表生成式的[]改成()，就创建了一个generator：

g=(i*i for i in range(11))
print(next(g))
print(next(g))
print(next(g))
print("=============================")
# 上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
gg=(i*i for i in range(6))
for n in gg:
    print(n)
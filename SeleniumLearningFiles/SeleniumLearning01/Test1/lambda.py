# 匿名函数lambda x: x * x实际上就是： def f(x):
    # return x * x
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。 匿名函数有个限制，
# 就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
f=lambda x:x*x
print(f(9))

# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y
print(build(2,0))

v=lambda x,y:x*x+y*y
print(v(1,3))
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
     print('2015-3-25')

# f1=now()
f2=now
print(f2())

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态
# 增加功能的方式，称之为“装饰器”（Decorator）。 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印
# 日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
        return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator
# 置于函数的定义处：
@log
def now():
    print('2015-3-25')
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志： >>>
now()
# call now():
# 2015-3-25



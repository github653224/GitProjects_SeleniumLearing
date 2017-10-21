# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用
# return语句返回。 我们以自定义一个求绝对值的my_abs函数为例：
def my_abs(x):
    if x>=0:
        print("走的大于零的分支")
        return x
    else:
        print("走的小于零的分支")
        return -x

a=my_abs(-99)
print(a)

b=my_abs(10)
print(b)

# 空函数
#  如果想定义一个什么事也不做的空函数，可以用pass语句：
def pop():
    pass

# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
#pass还可以用在其他语句里，比如：
age=0
if age >= 18:
    pass
# 缺少了pass，代码运行就会有语法错误。


# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。
# 所以，这个函数定义不够完善。 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用
# 内置函数isinstance()实现：

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("badtype")
    if x>=0:
        return x
    else:
        return -x

# 小结
 # 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。

# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义
# 出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

# 我们先写一个计算x2的函数：
def power(x):
    return x * x
# 对于power(x)函数，参数x就是一个位置参数。 当我们调用power函数时，必须传入有且仅有的一个参数x：
c=power(6)
print(c)


def power1(x,n):
    s=1
    while n>0:
        s*=x
        n-=1
    return s
print(power1(5,3))
print(power1(10,10))

# 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。 举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数：
# def enroll(name,gender):  #不带默认参数的函数
#     print("name:",name)
#     print("gender:",gender)
#
# enroll("panxueyan",F)


def enroll(name,gender,age=29,city="Beijing"):  #带默认参数的函数
    print("name:",name)
    print("gender:",gender)
    print("age:",age)
    print("city:",city)

enroll("panxueyan","F")




































































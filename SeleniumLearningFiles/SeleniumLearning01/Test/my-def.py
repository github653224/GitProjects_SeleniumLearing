def my_abs(x):
    if x>0:
        print("走了这一步")
        return x
    else:
        return abs(x) #return -x
print(my_abs(-99))

# 我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。
# 数据类型检查可以用内置函数isinstance()实现：

def my_abs(y):
    if not isinstance(y, (float)):
        raise TypeError('bad operand type')
    if y >= 0:
        return y
    else:
        return -y
print(my_abs(2.3))

def power1(x):
    return x*x
print(power1(-5))

# 现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？
# 我们不可能定义无限多个函数。 你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，
# 说干就干：
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2,3))

def enroll(name,gender):
    print("name:",name)
    print("gender:",gender)

print(enroll("panxueyan","28"))
print("1=============================")
print(list(range(11)))
# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
l=[]
for x in range(1,11):
    l.append(x*x)
print(l)
# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
s=[x * x for x in range(1, 12)]
print(s)
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，
# 十分有用，多写几次，很快就可以熟悉这种语法。for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print("2=======================")
a=[x*x for x in range(7) if x%2==0 ]
print(a)

# 还可以使用两层循环，可以生成全排列：
b=[m+n  for m in "ABC" for n in "abc"]
print(b)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,"=",v)


# 最后把一个list中所有的字符串变成小写：

L = ['Hello', 'World', 'IBM', 'Apple']
n=[s.lower() for s in L]
print(n)






















































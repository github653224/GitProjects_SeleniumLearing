def add(a,b):
    print(a+b)

add(2,3)

def add(c,d):    #通过return关键字返回结果，不会自动打印
    return c+d

print(add(4,8))

def add(e=1,f=9): #不传参数的默认参数的函数，如果不调用，那么add()函数就使用默认的参数进行计算
    return e-f

print(add())
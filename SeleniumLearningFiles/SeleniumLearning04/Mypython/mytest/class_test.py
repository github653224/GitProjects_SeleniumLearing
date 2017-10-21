class A():
    def __init__(self,a,b):     #init的两侧是双下划线，当我们在调用该类时，可以用来进行一些初始化工作
        self.a=int(a)
        self.b=int(b)
    def add(self):
        return self.a+self.b

count=A("4",5)
print(count.add())
#当我们调用A类时首先会执行的它的__init__方法，所以需要对其进行传参数。初始化所做的事情就是将输入的参数类型转换为int类型，这样
#可以在一定程度上保证程序的容错性。而add()方法可以直接拿初始化方法__init__()的self.a和self.b两个函数进行计算
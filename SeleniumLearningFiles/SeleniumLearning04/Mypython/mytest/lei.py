class A(object):
    def add(self,a,b):  #这个方法里的第一个参数必须是存在的，一般会命名为self，但是再调用这个方法时不需要为这个参数传值
        return a+b

count=A()
print(A().add(3,5))#通过类名点的方式调用类里的函数
print(count.add(4,6))

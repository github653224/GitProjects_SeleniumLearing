class Student ():
    pass

s1=Student()
s1.name="panxueyan"
print(s1.name)  #给实例绑定属性

# 给实例绑定方法如下：
from types import MethodType

def set_age(self,age):
    self.age=age

s1.set_age=MethodType(set_age,s1)
s1.set_age(18)
print(s1.age)

s2=Student()
# s2.set_age(230)
# print(s2.age)    发现不能给实例s2绑定方法，也就是给实例绑定方法只能用一次，要使其他的实例也能绑定方法，就需要给其类绑定方法
class Student ():
    pass

def  set_score(self,score):
    self.score=score

Student.set_score=set_score

s3=Student()
s3.set_score(22)
print(s3.score)

s4=Student()
s4.set_score(55)
print(s4.score)  #这里的实例s4再不用去绑定方法了



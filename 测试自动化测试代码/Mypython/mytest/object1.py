# 如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该
# 被视为一个对象，这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，
# 首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
class Student(object):
    def __init__(self,name,score):
        self.n=name
        self.s=score
    def print_score(self):
        print("%s:%s" % (self.n,self.s))

# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。面向对象的程序写出来就像这样：
Student("panxueyan",100).print_score()
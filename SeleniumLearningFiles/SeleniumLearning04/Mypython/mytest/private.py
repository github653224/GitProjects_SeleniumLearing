# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
# 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，
# 外部不能访问，所以，我们把Student类改一改：
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name=name

    def set_score(self,score):
        self.__score=score


bart=Student("panxueyan",99)
print(bart.get_name())

print(bart.get_score())

# bart.__name="haha"
bart.set_name("haha")
bart.set_score(88)
print(bart.get_name())
bart.print_score()
class student():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def print_score(self):
        print("%s:%d " % (self.__name,self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

bart=student("panxueyan",30)
# print(bart.name)
# print(bart.age)
# bart.print_score() #以上三个访问实例的属性会报错，原因是内部属性私有化了，加了__

print(bart.get_name())
print(bart.get_age())
bart.print_score()    #要访问实例私有属性就必须自在类部创建get__name,get__age方法








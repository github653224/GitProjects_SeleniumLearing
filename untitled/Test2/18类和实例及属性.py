class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_score(self):
        print("%s:%d " % (self.name,self.age))

bart=student("panxueyan",30)
print(bart.name)
print(bart.age)
bart.print_score()
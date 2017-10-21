class  TestCss:
	def __init__(self):
		self.a=0
		self.b=10
	def info(self):
		print(self.a ,self.b)
	def  define_a(self):
		self.c=19



if __name__=="__main__":
	# tc=TestCss()
	# tc.info()
	# tc.color="red"
	# print(tc.color)

	# tc=TestCss()
	# tca=TestCss()   
	# tc.a=100
	# tc.b=200
	# tc.info()
	# tca.info()  #结果不一样:相同类的不同实例属性是不相关的

	tc=TestCss()
	tc.define_a()
	print(tc.c) #会报错，因为没有对属性C进行实例初始化，在前面加上它的函数：define_a()，tc实例就有属性了
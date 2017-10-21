#类属性定义实例
class  TestCss:
	cssa="class-attribe" #类属性
	def __init__(self):
		self.a=0
		self.b=10
	def info(self):
		print(self.a  ,  self.b , TestCss.cssa) #类属性通过类名点引用


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
	tc.info()
	tca=TestCss()
	tca.info()
	TestCss.cssa=0
	tc.info()
	tca.info()             #类属性对于不同实例来说是一样的，不同于实例属性



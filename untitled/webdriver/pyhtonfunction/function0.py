class TestClassa:
	"""
	这是文档说明测试
	你知道吗
	"""
	def pr(self):
		self.height=20
		print(self.height)

tca=TestClassa()
tca.pr()


print(tca.__doc__) #类.__doc__可以调用出类的说明

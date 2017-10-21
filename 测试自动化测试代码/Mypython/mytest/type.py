# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
    pass

print(type(fn)==types.FunctionType)


print("abc".__len__())
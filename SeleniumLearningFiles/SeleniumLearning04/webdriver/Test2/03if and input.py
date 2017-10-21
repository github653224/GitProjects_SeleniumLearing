# 条件判断
#  计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。 比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现：
age=20
if age>18:
    print("your age is :",age)
    print("adult")
# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。 也可以给if添加一个else语句，
# 意思是，如果if判断是False，不要执行if的内容，去把else执行了：

age=3
if age>18:
    print("your age is :", age)
    print("adult")
else:
    print("your age is :",age)
    print("teenager")
# 注意不要少写了冒号:。 当然上面的判断是很粗略的，完全可以用elif做更细致的判断：
print("===========================================================")
age=3
if age>18:
    print("your age is :",age)
elif age>6:
    print("teenager")
else:
    print("kid")


# elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是： if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，
# 所以，请测试并解释为什么下面的程序打印的是teenager：


age=20
if age>18:
    print("adult")
elif age>6:
    print("teeenager")
else:
    print("kid")


# if判断条件还可以简写，比如写：
# if x:
#     print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False


# 再议 input
#  最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：
birth=int(input("please enter your birthdate:"))
if birth <2000:
    print("00前")
else:
    print("00后")

print("==========================================")
# 练习
#  小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数： •低于18.5：过轻
#  18.5-25：正常
#  25-28：过重
#  28-32：肥胖
#  高于32：严重肥胖
#  用if-elif判断并打印结果：

h=1.75
w=80.5
BIM=w/(h*h)
if BIM<18.5:
    print("体重过轻")
elif BIM>18.5 and BIM<25:
    print("体重正常")
elif BIM>25and  BIM<28:
    print("体重过重")
elif BIM>28 and BIM<32:
    print("肥胖")
else:
    print("严重肥胖")



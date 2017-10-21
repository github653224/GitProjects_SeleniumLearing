

#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names=["zhangsan","lisi","wangwu"]
for i in names:
    print(i)
# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
# 再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum=0
# for x in [1,2,3,4,5,6,7,8,9,10]:
#     # sum+=x
#     sum=sum+x
# print(sum)
# 或者如下
for x in range(1,11):
    sum=sum+x
print(sum)
print("0============================")
# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，
# 再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
print(range(5))
print(list(range(5)))

# for i in range(101):
#     print(i)
print("1=============================================================1")
sum=0
for i in range(101):
    sum=sum+i
print(sum)
# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
s="Hello"
for i in L:
    s=s+i
    print(s)
print(s)

#filter()过滤函数，可以把符合条件的过滤出来并返回True
def is_odd(n):
    return n % 2 == 1
s=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

print("2=============================================================2")
#字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print(d["Bob"])
print(d["Tracy"])

print("Bob" in d)
print(d.get("Bob"))
print("3====================================================3")
print(d)


d.pop("Michael")
print(d)
d["Bob"]=100
print(d)

print("4============================4")
# set集合
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：







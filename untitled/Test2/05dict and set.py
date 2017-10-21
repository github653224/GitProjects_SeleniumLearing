# dict
#  Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# 举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# 给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。 如果用dict实现
# ，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d["Michael"])
print(d["Bob"])

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉： >>> d['Jack'] = 90
# d['Jack']
# 90
# d['Jack'] = 88
# d['Jack']
# 88
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
d.pop("Michael")
print(d)

# set
#  set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。 要创建一个set，需要提供一
# 个list作为输入集合：
s=set([1,2,3,4])
print(s)

# 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。
# 。 重复元素在set中自动被过滤：
s1=set([1, 1, 2, 2, 3, 3,4,4])
print(s1)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s1.add(5)
print(s1)
# 通过remove(key)方法可以删除元素：
s1.remove(5)
print(s1)

























































# JSON
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来
# 就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接
# 在Web页面中读取，非常方便。
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON： >>>
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
print(d)

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。要把JSON反序列化为
# Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
print(json_str)










































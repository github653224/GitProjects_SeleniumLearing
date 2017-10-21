# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
e=["APPLE","BANNER",18,"ORAGE"]
f=[s.lower() for s in e  if isinstance(s,str)]
print(f)

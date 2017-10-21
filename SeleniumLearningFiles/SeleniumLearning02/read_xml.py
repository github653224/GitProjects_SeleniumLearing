from xml.dom import minidom
# 打开xml文档
dom = minidom.parse('info.xml')

# 得到文档元素对象
root = dom.documentElement

# print(root.nodeName)
# print(root.nodeValue)
# print(root.nodeType)
# print(root.ELEMENT_NODE)


# tagname = root.getElementsByTagName('browser')
# print(tagname[0].tagName)
#
# tagname = root.getElementsByTagName('login')
# print(tagname[1].tagName)
#
# tagname = root.getElementsByTagName('province')
# print(tagname[2].tagName)


logins = root.getElementsByTagName('login')

# 获得login标签的username属性值
username = logins[0].getAttribute("username")
print(username)

# 获得login标签的password属性值
password = logins[0].getAttribute("password")
print(password)

# 获得第二个login标签的username属性值
username = logins[1].getAttribute("username")
print(username)

# 获得第二个login标签的password属性值
password = logins[1].getAttribute("password")
print(password)


provinces = dom.getElementsByTagName('province')
citys = dom.getElementsByTagName('city')

# 获得第二个province标签对的值
p2 = provinces[1].firstChild.data
print(p2)

# 获得第一个city标签对的值
c1 = citys[0].firstChild.data
print(c1)

# 获得第二个city标签对的值
c2 = citys[1].firstChild.data
print(c2)


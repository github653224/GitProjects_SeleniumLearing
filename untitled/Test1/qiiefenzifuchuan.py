import re
# s='a b c'.split(' ')
# print(s)

f=re.split(r'\s+', 'a b c')
print(f)

m=re.match(r"(^\d{3})-(\d{3,8})","010-12345")
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.group(0))
print(m.group())










































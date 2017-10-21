from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from random import randint

verify =randint(1000,9999)

print(u"生成的随机数字： %d " %verify)

number=input("请输入随机数字：")
print(number)
number=int(number)

if number ==verify:
    print ("登录成功！！")
elif number==132741:
    print("登陆成功！！")
else:
    print("输入错误")

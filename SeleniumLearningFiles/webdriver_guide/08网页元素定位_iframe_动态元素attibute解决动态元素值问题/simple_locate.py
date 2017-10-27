# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.support.wait import WebDriverWait

if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Chrome()
dr.maximize_window()
file_path = 'file:///' + os.path.abspath('form.html')
print file_path



sleep(3)

# 以123邮箱为例
url = "http://www.126.com"
dr.get(url)
# 自动化登陆126邮箱时，遇到输入框元素被嵌入到iframe元素内，这时候用各种标签元素都是无法定位到输入框的，
# 这时候需要使用selenium中的方法进入到这个框架内，再使用定位：webdriver().switch_to.frame(index)

sleep(3)
dr.switch_to.frame(0)
username = "youxiang653224"
password = "youxiang6532244"
# # by name 这个利用by name 去定位已经成功 ，在利用找出改页面的id的属性值，因为这个id是动态的
input_email = dr.find_element_by_name('email')
id_attribute_value = input_email.get_attribute("id")
print id_attribute_value

# by id
dr.find_element_by_id(id_attribute_value).send_keys(username)

# by class name ,这里很特别class='j-inputtext dlpwd'，这里面有2个值，用其中一个就行
print 'start password'
dr.find_element_by_name('password').send_keys(password)
print "finish password"
sleep(10)
# by xpath 点击登录按钮
dr.find_element_by_xpath('//*[@id="dologin"]').click()

#点击登录按钮之后，出现验证码手工处理后再次点击登录
# sleep(10)
# dr.find_element_by_xpath('//*[@id="dologin"]').click()

sleep(6)
id_attribute_value =  dr.find_element_by_xpath('//*[@id="_mail_tabitem_6_58text"]').get_attribute('id')
#'_mail_tabitem_6_58text'
print id_attribute_value

dr.find_element_by_id(id_attribute_value).click()
dr.refresh()
# selenium 提供switch_to_alert()方法定位到 alert/confirm/prompt对话框。
# 使用 text/accept/dismiss/send_keys 进行操作，这里注意的是send_keys只能对prompt进行操作。
# switch_to_alert() 　　#定位弹出对话
# text() 　　                #获取对话框文本值
# accept()                   #相当于点击"确认"
# dismiss()                  #相当于点击"取消"
# send_keys()              # 输入值，这个alert和confirm没有输入对话框，所以这里就不能用了，所以这里只能使用在prompt这里
# dr.switch_to.alert().dismiss()
sleep(5)



dr.quit()
# dr.get(file_path)
# by id
# dr.find_element_by_id('inputEmail').send_keys("haha")
# dr.switch_to.frame(0)
# dr.find_element_by_name('email').send_keys("haha")

# # by name
# dr.find_element_by_name('password').click()
#
# # by tagname
# print dr.find_element_by_tag_name('form').get_attribute('class')
#
# # by class_name
# e = dr.find_element_by_class_name('controls')
# dr.execute_script('$(arguments[0]).fadeOut().fadeIn()', e)
# sleep(1)
#
# # by link text
# link = dr.find_element_by_link_text('register')
# dr.execute_script('$(arguments[0]).fadeOut().fadeIn()', link)
# sleep(1)
#
# # by partial link text
# link = dr.find_element_by_partial_link_text('reg')
# dr.execute_script('$(arguments[0]).fadeOut().fadeIn()', link)
# sleep(1)
#
# # by css selector
# div = dr.find_element_by_css_selector('.controls')
# dr.execute_script('$(arguments[0]).fadeOut().fadeIn()', div)
# sleep(1)
#
# # by xpath
# dr.find_element_by_xpath('/html/body/form/div[3]/div/label/input').click()
#
# sleep(5)
# dr.quit()
#






































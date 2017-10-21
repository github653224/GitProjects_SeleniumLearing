from selenium import webdriver
import time
class Login():
    # 登录
    def user_login(self,driver,username,password):
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(username)
        time.sleep(3)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        time.sleep(3)
        driver.find_element_by_id("dologin").click()
        time.sleep(8)
        driver.find_element_by_class_name("gWel-mailInfo-txt").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="_mail_component_70_70"]/span[2]').click()

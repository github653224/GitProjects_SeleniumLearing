from selenium import webdriver
from public00 import Login
import time
#设置不同用户的登陆：
"""
pan944851899/panxueyan123
pan653224/panxueyan123
panxueyan653224/panxueyan123
"""
class LoginTest():
    def __init__(self):
        # self.driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
        self.driver=webdriver.Ie(executable_path = 'C:\\Program Files\\Internet Explorer\\IEDriverServer.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://www.126.com")
        self.driver.switch_to.frame("x-URS-iframe")

    def guest01_login(self):
        username="pan944851899"
        password="panxueyan123"
        Login().user_login(self.driver,username,password)
        time.sleep(10)
        self.driver.quit()

    def guest02_login(self):
        username = "pan653224"
        password = "panxueyan123"
        Login().user_login(self.driver, username, password)
        self.driver.quit()

    def guest03_login(self):
        username = "panxueyan653224"
        password = "panxueyan123"
        Login().user_login(self.driver, username, password)
        self.driver.quit()

A = LoginTest()
A.guest01_login()
# A.guest02_login()
# A.guest03_login()





#
# # 调用登录模块
# Login().user_login(driver)
#
# # 收信、写信、删除信件等操作
# # ……
#
# # 调用退出模块
# Login().user_logout(driver)
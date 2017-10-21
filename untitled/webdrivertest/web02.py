from webbrowser import Chrome
from selenium import webdriver
import os,time
class Test():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
    def open_url(self):
        self.driver.get("http://www.cnblogs.com")
        self.driver.maximize_window()
        time.sleep(3)

    def login_user(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("input1").send_keys("Halo3224")
        self.driver.find_element_by_id("input2").send_keys("panxueyan653224.")
        self.driver.find_element_by_class_name("button").click()

    def get_title(self):
        # print(self.driver.get_cookie())
        print(self.driver.title)

    def wait_time(self):
        time.sleep(10)

    def quit_out(self):
        self.driver.quit()


op=Test()
op.open_url()
op.login_user()
op.get_title()
op.quit_out()

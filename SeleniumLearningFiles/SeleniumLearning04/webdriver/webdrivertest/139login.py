from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class Login_Test0():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')

    def open_url(self):
        self.driver.maximize_window()
        self.driver.get("http://m.mail.10086.cn")
    def type_username(self):
        self.driver.find_element_by_id("ur").send_keys("18010193189")
        self.driver.find_element_by_id("pw").send_keys("panxueyan123")
        sleep(10)
    def click_login(self):
        self.driver.find_element_by_id("lnkSubmit").click()
        sleep(5)

    def login_out(self):
        self.driver.find_element_by_id("logout").click()
        sleep(10)
        self.driver.quit()
b=Login_Test0()
b.open_url()
b.type_username()
b.click_login()
b.login_out()

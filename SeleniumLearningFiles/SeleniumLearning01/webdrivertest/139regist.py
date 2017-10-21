from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class Login_Test():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')

    def open_url(self):
        self.driver.maximize_window()
        self.driver.get("http://m.mail.10086.cn")

    def regist(self):
        self.driver.find_element_by_xpath('//*[@id="w3form"]/div/div[2]/p/a[1]').click()
        self.driver.find_element_by_id("phone").send_keys("18010193189")
        self.driver.find_element_by_xpath("/html/body/article/section/article/section/fieldset/form/ul/li[5]/a").click()
        sleep(20)
        self.driver.find_element_by_id("po").send_keys("panxueyan123")
        sleep(60)

    def comfoirmregist(self):
        self.driver.find_element_by_id("sendsubmit").click()


a=Login_Test()
a.open_url()
a.regist()
a.comfoirmregist()


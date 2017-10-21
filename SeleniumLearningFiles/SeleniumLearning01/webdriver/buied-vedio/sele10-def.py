from selenium import webdriver
import time

url="http://maiziedu.com"
account="18010193189"
pwd="panxueyan653224."
login_text="登录"

class test():

    def __init__(self):
        self.driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="div_company_mini"]/div[4]').click()#去掉自动弹框

    def longin_test(self):
        self.driver.find_element_by_link_text(login_text).click()
        time.sleep(5)
        self.driver.find_element_by_id("id_account_l").clear()
        self.driver.find_element_by_id("id_account_l").send_keys("18010193189")
        time.sleep(3)
        self.driver.find_element_by_id("id_password_l").clear()
        self.driver.find_element_by_id("id_password_l").send_keys("panxueyan653224.")
        time.sleep(3)
        self.driver.find_element_by_id("login_btn").click()
        try:
            self.driver.find_element_by_link_text("该账号格式不正确")
            print("请输入正确的账号")
        except:
            print("登录成功")
        time.sleep(3)

    def login_out(self):
        self.driver.find_element_by_class_name("sign_out").click()
        time.sleep(5)
        self.driver.quit()



b=test()
b.longin_test()
b.login_out()

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.maiziedu.com")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="div_company_mini"]/div[4]').click()
time.sleep(3)
driver.find_element_by_link_text("登录").click()
driver.implicitly_wait(5)
driver.find_element_by_id("id_account_l").send_keys("18010193189")
time.sleep(3)
driver.find_element_by_id("id_password_l").send_keys("panxueyan653224.")
driver.find_element_by_id("login_btn").click()
time.sleep(3)
driver.find_element_by_class_name("sign_out").click()
time.sleep(10)
driver.quit()

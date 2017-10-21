from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.baidu.com")

driver.find_element_by_id('kw').send_keys("seleniumm")
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)#删除多输入的一个m

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"A")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"X")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"V")
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")
driver.find_element_by_id("su").send_keys(Keys.ENTER)



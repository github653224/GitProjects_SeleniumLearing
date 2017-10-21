from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
driver.get("http://www.baidu.com")

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

driver.get_screenshot_as_file("D:\\baidu_img.jpg")
driver.quit()

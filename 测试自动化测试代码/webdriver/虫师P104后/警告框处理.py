from selenium import webdriver
import time,os

from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.baidu.com")

#把鼠标移至设置的连接上面
link=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()
time.sleep(3)

driver.find_element_by_link_text("搜索设置").click()
time.sleep(5)
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(5)

driver.switch_to.alert.accept()


time.sleep(6)
driver.quit()


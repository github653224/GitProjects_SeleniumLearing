from selenium import webdriver
import time,os
driver=webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
file_path='file:///'+os.path.abspath(r"E:\Users\Administrator\PycharmProjects\webdriver\虫师P104后\frame.html")
driver.get(file_path)
# driver.quit()
driver.switch_to.frame("if") #切换表单至frame:switch().to.frame()如果没有这句话，就找不到相应的元素
driver.find_element_by_id("kw").send_keys("潘雪岩")
driver.find_element_by_id("su").click()
time.sleep(10)
driver.quit()
from  selenium import webdriver
import time,os
driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
# file_path='file:///'+os.path.abspath("D:\\Users\\Administrator\\PycharmProjects\\untitled\\webdrivertest\\fileup.html")
driver.maximize_window()
# driver.get(file_path)
driver.get("http://localhost//fileup.html")
driver.implicitly_wait(10)
driver.find_element_by_name("file").send_keys("D:\\Users\\Administrator\\PycharmProjects\\untitled\\webdrivertest\\test.txt")
time.sleep(10)
driver.quit()
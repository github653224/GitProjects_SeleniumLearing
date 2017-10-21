from selenium import webdriver
import time

driver=webdriver.Ie(executable_path = 'E:\\webdriver\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.126.com")
driver.refresh()
time.sleep(10)
#
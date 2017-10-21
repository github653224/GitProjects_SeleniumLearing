from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time,os
# driver=webdriver.Ie(executable_path = 'E:\\webdriver需要的\\IEDriverServer_Win32_2.53.1\\IEDriverServer.exe')
driver=webdriver.Ie(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
# driver.switch_to_alert().accept()
# driver.switch_to_alert().dismiss()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.quit()

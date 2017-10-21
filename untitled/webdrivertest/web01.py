from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time,os
# driver=webdriver.Ie(executable_path = 'E:\\webdriver需要的\\IEDriverServer_Win32_2.53.1\\IEDriverServer.exe')
driver=webdriver.Ie(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
file_path =  'file:///' + os.path.abspath('D:\\Users\\Administrator\\PycharmProjects\\untitled\\webdrivertest\\test00.html')


print(os.path.dirname('D:\\Users\\Administrator\\PycharmProjects\\untitled\\webdrivertest\\test00.html'))
print(os.path.basename('D:\\Users\\Administrator\\PycharmProjects\\untitled\\webdrivertest\\test00.html'))
print(os.path.exists('D:\\Users\\Administrator\\PycharmProjects\\untitled\\webdrivertest\\test00.html'))


driver.maximize_window()
driver.get(file_path)
time.sleep(2)
m=driver.find_element_by_id("ShippingMethod")
m.find_element_by_xpath("//option[@value='10.69']").click()
time.sleep(3)
driver.quit()
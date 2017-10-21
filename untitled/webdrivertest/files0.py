from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time,os
# driver=webdriver.Ie(executable_path = 'E:\\webdriver需要的\\IEDriverServer_Win32_2.53.1\\IEDriverServer.exe')
driver=webdriver.Ie(executable_path = 'E:\\webdriver\\chromedriver_win32\\chromedriver.exe')

driver.get("https://www.baidu.com")
driver.maximize_window()
driver.refresh()
driver.find_element_by_id("kw").send_keys("周杰伦")
time.sleep(6)
driver.find_element_by_id("su").send_keys(Keys.ENTER)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
driver.find_element_by_id("kw").send_keys("潘雪岩")
driver.find_element_by_id("su").submit()


# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_id("TANGRAM__PSP_8__userName").clear()

print(driver.title)
driver.implicitly_wait(10)

# driver.quit()

# driver.get("https://pan.baidu.com/")
# driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("944851899@qq.com")
# driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("123")
# driver.find_element_by_id("TANGRAM__PSP_4__submit").submit()
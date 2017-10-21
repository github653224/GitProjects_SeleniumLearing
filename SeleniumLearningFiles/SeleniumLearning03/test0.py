from selenium import webdriver
from datetime import datetime
import time

# driver=webdriver.Firefox(executable_path = 'C:\Program Files\Mozilla Firefox\geckodriver.exe')
# driver=webdriver.Ie(executable_path = 'C:\Program Files\Internet Explorer\IEDriverServer.exe')
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.baidu.com")
driver.maximize_window()
print("设置浏览器的宽 480 高 800显示")
# driver.set_window_size(480,800)


driver.find_element(By.ID,"kw").send_keys("刘亦菲")
time.sleep(3)
print("clicked")
driver.find_element(By.ID,"su").click()
time.sleep(3)

driver.back()
time.sleep(5)
driver.forward()

driver.set_window_size(500,400)
time.sleep(8)
driver.maximize_window()#窗口最大化
tl=driver.title #得到浏览器的标题
print(tl)

time.sleep(6)
driver.refresh()

driver.find_element_by_id("kw").clear()
driver.implicitly_wait()


# driver.quit() #退出浏览器引擎
#driver.close()  #关闭浏览器



























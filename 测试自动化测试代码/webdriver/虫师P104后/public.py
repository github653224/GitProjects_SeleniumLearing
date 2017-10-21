from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
driver.delete_all_cookies()
driver.maximize_window()
driver.get("http://www.126.com")

# driver.refresh()
time.sleep(3)
# driver.switch_to_frame()

driver.implicitly_wait(10)
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("pan944851899")
driver.find_element_by_name("password").send_keys("panxueyan123")
time.sleep(10)
driver.find_element_by_id("dologin").click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector('a[title="关闭"]').click()
driver.find_element_by_xpath(".//*[@ href='javascript:;']")





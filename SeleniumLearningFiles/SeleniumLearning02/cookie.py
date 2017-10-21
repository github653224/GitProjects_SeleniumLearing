from selenium import webdriver
import time
driver=webdriver.Chrome(r"C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("panxueyan")
driver.find_element_by_id("su").click()
time.sleep(4)

driver.set_window_size(600,600)
js="window.scrollTo(100,1000);"
time.sleep(5)
driver.execute_script(js)
# driver.quit()


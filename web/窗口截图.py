from selenium import webdriver
import time
driver=webdriver.Chrome(r"C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("panxueyan")
driver.find_element_by_id("su").click()

time.sleep(4)
driver.get_screenshot_as_file(r"D:\Users\Administrator\PycharmProjects\web\baidu.png")
driver.quit()
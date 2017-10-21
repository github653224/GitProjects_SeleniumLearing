from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("麦子学院")
driver.find_element_by_id("su").click()
time.sleep(3)
# driver.find_element_by_partial_link_text("百度百科").click()
driver.find_element_by_partial_link_text(" - 专业IT职业在线教育平台|ui设计培训|python...").click()

print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)

driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
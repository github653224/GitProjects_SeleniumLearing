from selenium import webdriver
import time
search_text=["python","中文","text"]
for text in search_text:
    driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(text)
    driver.find_element_by_id("su").click()
time.sleep(10)
driver.quit()


from selenium import webdriver
driver=webdriver.Chrome(r"C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
driver.maximize_window()
driver.get("http://youdao.com")
cookie=driver.get_cookies()
print(cookie)

driver.quit()


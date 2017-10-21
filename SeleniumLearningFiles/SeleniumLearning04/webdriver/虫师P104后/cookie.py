from selenium import webdriver
driver=webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.baidu.com")
cookies=driver.get_cookies()
print(cookies)
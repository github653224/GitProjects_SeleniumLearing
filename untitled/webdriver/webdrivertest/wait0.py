from selenium import webdriver
from time import ctime , sleep

driver=webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.baidu.com")
print(ctime())

for i in range(10):
    try:
        el=driver.find_element_by_id("kw22")
        if el.is_displayed():
            break
    except: pass
    sleep(1)
else:
        print("time is out")

driver.quit()

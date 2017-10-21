from selenium import webdriver
from time import ctime

from selenium.common.exceptions import NoSuchElementException

driver= webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
print(ctime())
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")
print(ctime())
try:
    driver.find_element_by_id("kw").send_keys("a")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()

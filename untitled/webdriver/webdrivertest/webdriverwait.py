# from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.baidu.com")
driver.maximize_window()

element=WebDriverWait(driver,5,0.5).until(
    EC.presence_of_element_located((By.ID,"kw"))
)

element.send_keys("slenium")
driver.quit()



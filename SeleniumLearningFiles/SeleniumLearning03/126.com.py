from selenium import webdriver
import time

# driver=webdriver.Firefox(executable_path = 'C:\Program Files\Mozilla Firefox\geckodriver.exe')
driver=webdriver.Ie(executable_path = 'C:\Program Files\Internet Explorer\IEDriverServer.exe')
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("http://www.126.com")
driver.maximize_window()
driver.find_element_by_id("idInput").send_keys("panxueyan3224")
from telnetlib import EC
from selenium import webdriver
from datetime import datetime
import time
driver=webdriver.Firefox(executable_path = 'C:\Program Files\Mozilla Firefox\geckodriver.exe')
# driver=webdriver.Ie(executable_path = 'C:\Program Files\Internet Explorer\IEDriverServer.exe')
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# driver=webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.refresh()



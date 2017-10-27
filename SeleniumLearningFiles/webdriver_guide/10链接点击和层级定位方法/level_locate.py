# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr = webdriver.Chrome()
dr.maximize_window()
file_path =  'file:///' + os.path.abspath('level_locate.html')
dr.get('http://localhost:8080/myhtml/level_locate.html')

time.sleep(5)

print 'start click link1'
dr.find_element_by_link_text('Link1').click()
print 'end click link1'

print 'start is displayed'
dr.refresh()
WebDriverWait(dr, 60).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())
print 'end displayed'

menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Another action')

webdriver.ActionChains(dr).move_to_element(menu).perform()

time.sleep(2)

dr.quit()


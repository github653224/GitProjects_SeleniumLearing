from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(5)
# driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部

# driver.execute_script("$('.fileinput-button input').eq(0).attr('style','height:20px;opacity:1;display:block;position:static;transform:translate(0px, 0px) scale(1)')")
driver.find_element_by_name('tj_settingicon').click()

# ActionChains(driver).move_to_element(above).perform()

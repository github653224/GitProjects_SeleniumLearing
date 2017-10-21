from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://yunpan.360.cn")
# driver.refresh()
# driver.implicitly_wait(3)
driver.find_element_by_name("account").send_keys("944851899@qq.com")
driver.find_element_by_name("password").send_keys("panxueyan653224.")
driver.find_element_by_xpath('//*[@id="login"]/div/div[2]/form/p[5]/input').submit()
# driver.find_element_by_xpath('//*[@id="BasePanel1"]/div/div[3]/span').click()

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("as")
driver.find_element_by_id("su").click()

link =driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
driver.find_element_by_link_text("搜索设置").click()

driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/span').click()
# driver.find_element_by_css_selector("span[title=\"关闭\"]").click()
# driver.find_element_by_class_name("pfpanelclose close briiconsbg").click()
time.sleep(2)

driver.switch_to_alert().accept()
# driver.quit()


# '//*[@id="auto-id-1479353985711"]'
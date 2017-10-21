from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.maiziedu.com")

# driver.find_element_by_link_text("iOS 应用开发").click()
# driver.find_element_by_link_text("iOS 应用开发").send_keys(Keys.ENTER)

ActionChains(driver).move_to_element(driver.find_element_by_link_text("iOS 应用开发")).perform()

# driver.quit()
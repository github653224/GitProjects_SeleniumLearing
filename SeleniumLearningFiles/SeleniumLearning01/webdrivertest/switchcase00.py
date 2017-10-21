from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.maximize_window()

sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

all_handles=driver.window_handles

for handle in all_handles:
    if handle !=sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("userName").send_keys('username')
        driver.find_element_by_name("password").send_keys('password')
        time.sleep(2)

for handle in all_handles:
    if handle==sreach_windows:
                driver.switch_to.window(handle)
                print('now sreach window!')
                driver.find_element_by_id('TANGRAM_PSP__2__cloesBtn').click()
                driver.find_element_by_id("kw").send_keys('selenium')
                driver.find_element_by_name("su").click()
                time.sleep(2)
driver.quit()

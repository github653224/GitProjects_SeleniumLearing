from selenium import webdriver
import time,os
driver=webdriver.Chrome(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

#获得百度搜索框句柄
sreach_windows=driver.current_window_handle
print(sreach_windows)

driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()


#获得当前所有打开的窗口的句柄
all_handles=driver.window_handles
print(all_handles)
# driver.quit()
#进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        print("now register window !")
        driver.find_element_by_name("userName").send_keys("username")
        driver.find_element_by_name("password").send_keys("password")
        time.sleep(3)
#又一次返回到搜素窗口
for handle in all_handles:
    if handle==sreach_windows:
        driver.switch_to.window(handle)
        print("now start research")
        driver.find_element_by_id("TANGRAM__PSP_2__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("panxueyan")
        driver.find_element_by_id("su").click()
        time.sleep(3)

# driver.quit()


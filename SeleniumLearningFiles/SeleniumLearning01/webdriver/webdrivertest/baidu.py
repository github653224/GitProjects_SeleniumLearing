from  selenium import webdriver
import time
driver=webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.baidu.com")
driver.maximize_window()
size=driver.find_element_by_id("kw").size #获取输入框的尺寸
print(size)

text=driver.find_element_by_id("cp").text #返回百度页面底部备案信息
print(text)

attribute=driver.find_element_by_id("kw").get_attribute("type")#返回元素的属性值，可以是id/name/type或者其他属性
print(attribute)

result=driver.find_element_by_id("kw").is_displayed() #返回元素结果是否可见，返回结果为True或者False
print(result)
time.sleep(5)
driver.quit()
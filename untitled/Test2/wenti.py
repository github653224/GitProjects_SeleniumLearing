# _*_ coding=utf-8 _*_
from selenium import webdriver
import unittest, time
from time import sleep

class WebTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
        print ('Test Start....')

    def tearDown(self):
        self.driver.quit()
        print ('Test End')

    def test_1(self):
        '''点击优品,进入优品详情，验证'''
        self.driver.get("http://www.hyuntao.com/wxpay104/10000/hyt/mainPage")
        '''点击传承，验证老字号是否存在'''
        js = "$(\'a[class=\"newpg in_pg3\"]\').click()"
        self.driver.execute_script(js)
        for i in range(60):
            try:
                result1 = self.driver.find_element_by_css_selector( 'img[href = "http://hyt-test.oss-cn-hangzhou.aliyuncs.com/companywap/images/img_laozihao.jpg"]').text
                print (result1)
                self.assertTrue('laozihao' in result1)
                break
            except:
                pass
            sleep(1)
        else:
            self.driver.get_screenshot_as_file("D:\\Job\\python\\code\\Hyt\\Not_loggoin\\pic\\error_pic_004.png")
            self.fail('验证失败')
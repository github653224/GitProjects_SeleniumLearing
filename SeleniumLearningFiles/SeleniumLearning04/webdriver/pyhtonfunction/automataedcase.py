import unittest
import HTMLTestRunner
import os
import time

listaa='E:\\Users\\Administrator\\PycharmProjects\\webdriver\\webdrivertest\\test0.py'  #设置脚本所在的绝对路径
def createsuitel():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa, pattern='UnitTestHtml_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print (testunit)
    return testunit
alltestnames=createsuitel()
#now=time.strftime('%Y-%m-%M-%H_%M_%S',time.localtime(time.time()))  #时间格式有错误
now=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time())) #设置时间格式
fp = open(now+'result.html','wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'result:') #调用HTMLRestRunner

k=1
while k<2:
    timing=time.strftime('%H_%M',time.localtime(time.time()))
    if timing == '12_31':  #17_35指17:35,这个可以根据需要设定时间
        print ('start to run scripts')
        runner.run(alltestnames) #运行所有的case
        print ('Finish runing scripts')
        break
    else:
        time.sleep(3)
        print (timing)
fp.close()
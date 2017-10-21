import unittest
class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp,每次先执行我啊')

    def tearDown(self):
        print('tearDown...每次后执行我啊')

a=TestDict()

a.setUp()
a.tearDown()

def A():
    print("执行开始")
A()


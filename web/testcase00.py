from calculator import Count
import  unittest
class TestCount(unittest.TestCase):
    def setUp(self):
        print("testadd is starting")
    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add02(self):
        j=Count(10,100)
        self.assertEqual(j.add(),110)
    def tearDown(self):
        print("testadd is end")



class TestSub(unittest.TestCase):
    def setUp(self):
        print("testsub is starting")
    def test_sub(self):
        j=Count(2,3)
        self.assertEqual(j.sub(),-1)
    def test_sub02(self):
        j=Count(10,4)
        self.assertEqual(j.sub(),6)
    def tearDown(self):
        print("testsub is end")

if __name__=='__main__':
    suite=unittest.TestCase()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add02"))


    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub02"))
    runner=unittest.TextTestRunner()
    runner.run(suite)


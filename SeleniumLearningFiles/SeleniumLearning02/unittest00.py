from calculator import Count
class TestCount:
    def test_add(self):
        try:
            j=Count(2,3)
            add=j.add()
            assert(add==5)
        except ArithmeticError as msg:
            print(msg)
        else:
            print("test pass")

mytest=TestCount()
mytest.test_add()

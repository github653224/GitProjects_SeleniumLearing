f=open("E:\\test\\test.txt","r")
print(f.read())
f.close()
#最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能
# 打开的文件数量也是有限的：

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，
# 我们可以使用try ... finally来实现：
try:
    f1=open(r"E:\test\test1.txt","r")
    print(f1.read())
finally:
    if f:
        f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
print("=================================================================================================")
with open("E:\\test\\test.txt","r") as f:
    print(f.read())




































#将A文件的内容写入到B文件中
import os
from webdrivertest.feice00 import readDataFromTxt
from webdrivertest.file02 import writeDataToTxt


def writeAFile2BFile(aPath,bPath):
    mytxt=readDataFromTxt(aPath)
    if mytxt:                                   #调用方法读取A文件（txt）的内容
        print ("A中的内容：\n" +mytxt)
        writeDataToTxt(bPath,mytxt)             #调用方法往B文件（txt）写入内容
        mytxtB=readDataFromTxt(bPath)
        print ("B中的内容：\n" +mytxtB)
    else:
        print ("提示：A中的内容为空：\n")
#主函数

if __name__ == '__main__':
    currentPath=os.getcwd()                    #获取当前路径
    aPath =currentPath+"\\A.txt"               #拼接A文件的路径
    bPath =currentPath+"\\B.txt"
    writeAFile2BFile(aPath,bPath)
    pass
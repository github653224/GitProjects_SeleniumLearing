import os

#从文本（txt）中读内容
def readDataFromTxt(path):
    contents=""
    if os.path.exists(path):
        try:
            fr=open(path,'r')
            contents=fr.read()
            print(contents)
            fr.close()
        except IOError:
            print("提示：A文件不存在，或者读取出现异常！")
    else:
        print ("提示：文件"+path+"不存在，请输入正确路径！")
    return contents

# file0=readDataFromTxt("E:\\test\\test1.txt")
# file0=readDataFromTxt("E:\\test\\test.txt")


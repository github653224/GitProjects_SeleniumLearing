import os
#将内容写入到指定文件（txt）中
def writeDataToTxt(path,mytxt): #这里path指的是文件的路径和文件名，mytxt是要往里面写的内容
    if os.path.exists(path):
        try:
            fw=open(path,'a+')
            fw.write(mytxt+"\n")
            fw.close()
        except IOError:
            print ("提示：B文件不存在，或者读取出现异常！")
    else:
        print ("提示：文件"+path+"不存在，创建该文件！")
        fw=open(path,"a+")
        fw.write(mytxt+"\n")
        fw.close()
# file0=writeDataToTxt("E:\\test\\test1.txt","haha21")
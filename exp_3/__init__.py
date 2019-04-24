# coding=UTF-8

import os

allFileNum = 0


def printPath(level, path):
    global allFileNum
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []

    fileList = []

    files = os.listdir(path)

    # 先添加目录级别
    dirList.append(str(level))

    for f in files:
        if(os.path.isfile(path+'/'+f)):
            fileList.append(f)

    for fl in fileList:
        print '-' * (int(dirList[0])),fl
        allFileNum = allFileNum + 1


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%S%s' % (filepath, allDir))
        print child.decode('gbk')



if __name__ == '__main__':
    # filePath = "E:\\myCourse\\大数据\\Dataset\\20newsgroups\\alt.atheism\\"
    printPath(1, "E:\\myCourse\\大数据\\Dataset\\20newsgroups\\alt.atheism")
    print allFileNum
    # eachFile(filePath)
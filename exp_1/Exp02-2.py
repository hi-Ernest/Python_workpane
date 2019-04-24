#!/usr/bin/env python
# coding: utf-8


# In[3]:

import os


path='E:\Python_workpane/Dataset/20newsgroups'

dirlist = []

filelist = []

dic = {}

dirlist = os.listdir(path)


for dl in dirlist:
    filelist=os.listdir(path+'/'+dl)
    for fl in filelist:
        text = open(path+'/'+dl+'/'+fl, 'r', errors='ignore').read()
        # errors='ignore'忽略非法字符
        text = (text.replace(',', ' ').replace('(', ' ').replace(')', ' ').replace('<',' ').replace('>',' ').replace('@',' ').replace('.',' ').replace('*',' ').lower()).split()
        for word in text:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1


file=open('E:\Python_workpane/top100_20newsgroup.txt','w')
L = sorted(dic.items(), key=lambda item:item[1], reverse=True)  # 按value升序排序
L = L[:100]  # 取前100个
for i in L:
    file.write(str(i)+'\n')
file.close()
'''
for i in dic:
    file.write(i+'：'+str(dic[i])+'\n')
file.close()
'''


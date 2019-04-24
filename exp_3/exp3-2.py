# coding: utf-8


import os
import re
import jieba
import math
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path='E:/myCourse/Dataset/20newsgroups'
dirlist=[]
filelist=[]
wordlist=[]
AllWordDic={}
dirlist=os.listdir(path)
for dl in dirlist:
    filelist=os.listdir(path+'/'+dl)
    break  # 此处只处理了一个文件夹里的文件

for fl in range(0,3):
    new_text = []

    text=open(path+'/'+dl+'/'+filelist[fl], 'r').read().lower()

    # 利用jieba分词

    text = list(jieba.cut(text))
    for w in text:
        #去除非英文字母
        if w.isalpha():
            new_text.append(w)

    for word in new_text:
        if word not in wordlist:
            wordlist.append(word)
        if word in AllWordDic:
            AllWordDic[word]+=1
        else:
            AllWordDic[word]=1

#初始化词向量矩阵
tfid_table=[[0 for col in range(0,len(wordlist))] for row in range(0,len(filelist))]


for dl in dirlist:
    filelist=os.listdir(path+'/'+dl)
    break#此处只处理了一个文件夹里的文件
for fl in range(0,3):
    new_text=[]
    text=open(path+'/'+dl+'/'+filelist[fl],'r').read().lower()#errors='ignore'忽略非法字符
    #利用jieba分词
    text=list(jieba.cut(text))
    for w in text:
        #去除非英文字母
        if w.isalpha():
            new_text.append(w)
    dic={}
    for word in new_text:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
    for t in range(0,len(wordlist)):
        if wordlist[t] in dic:
            tfid_table[fl][t]+=dic[wordlist[t]]

'''
for fl in range(0,len(filelist)):
    for w in range(0,len(wordlist)):
        print(str(tfid_table[fl][w])+"   ",end='')
    print('\n')
'''

tfidf=[[0 for col in range(0,len(wordlist))] for row in range(0,len(filelist))]
N=len(filelist)
for i in range(0, len(wordlist)):
    dfi = 0
    for j in range(0, len(filelist)):
        if tfid_table[j][i] != 0:
            dfi += 1
    for k in range(0, len(filelist)):
        tfidf[k][i] = tfid_table[k][i] * math.log(N/dfi)
'''
for fl in range(0,len(filelist)):
    for w in range(0,len(wordlist)):
        print(str(tfidf[fl][w])+"   ",end='')
    print('\n')
'''

wordCloud_dic = {}
for w in range(0,len(wordlist)):
    wordCloud_dic[ wordlist[w] ]=tfidf[0][w]

IMG = np.array(Image.open("E:\\Python_workpane\\test\\chr4.jpg"))
wordcloud = WordCloud(font_path = "simsun.ttc",mask=IMG,background_color='white',scale=5)
wordcloud.generate_from_frequencies(wordCloud_dic)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
wordcloud.to_file("E:/myCourse/Dataset/20newsgroups/wordcloud.png")
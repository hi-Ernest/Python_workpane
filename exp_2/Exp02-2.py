# -*- coding: utf-8 -*-
import os
path='E:\Python_workpane/Dataset/20newsgroups'
dirlist=[]
filelist=[]
dic={}
dirlist=os.listdir(path)

print('Processing text dataset')

texts = []
labels_index = {}
labels = []

for name in sorted(os.listdir(dir)):
    path = os.path.join(dir, name)
    if os.path.isdir(path):
        label_id = len(labels_index)
        labels_index[name] = label_id  # 每个文件夹给一个ID
        for fname in sorted(os.listdir(path)):
            if fname.isdigit():
                fpath = os.path.join(path, fname)
                if sys.version_info < (3,):
                    f = open(fpath)
                else:
                    f = open(fpath, encoding='latin-1')
                texts.append(f.read())
                f.close()
                labels.append(label_id)
print('Found %s texts.' % len(texts))


for dl in dirlist:
    filelist=os.listdir(path+'/'+dl)
    for fl in filelist:
        text=open(path+'/'+dl+'/'+fl,'r',errors='ignore').read()
        #errors='ignore'忽略非法字符
        text=(text.replace(',',' ').replace('(',' ').replace(')',' ').replace('<',' ').replace('>',' ').replace('@',' ').replace('.',' ').replace('*',' ').lower()).split()
        for word in text:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1


file=open('E:\Python_workpane/top500_20newsgroup.txt','w')
L = sorted(dic.items(),key=lambda item:item[1],reverse=True)#按Vvalue升序排序
L = L[:500]#取前500个
for i in L:
    file.write(str(i)+'\n')
file.close()
'''
for i in dic:
    file.write(i+'：'+str(dic[i])+'\n')
file.close()
'''

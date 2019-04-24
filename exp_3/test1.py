# *- coding: utf-8 -*-
'''
Created on 2018年10月24日
@author: pureyang
@description：
'''

import jieba
import math

# 实现分词
def fenci(s):
    seg_list = jieba.cut(s)
    result = []
    for seg in seg_list:
        seg = ''.join(seg.split())
        if (seg != '，' and seg != '？'and seg != '。' and seg != "\n" and seg != "\n\n"):
            result.append(seg)
    return result

# 计算每个词在每段文本中的次数
def getCount(data):
    docCount = list()
    for i, word in enumerate(data):
        vec = dict()
        for w in word:
            if not vec.get(w):
                vec[w] = 1
            else:
                vec[w] += 1
        docCount.append(vec)
    return docCount

# 计算tf的值
def tf(data):
    tf_word = []
    for i, doc in enumerate(data):
        docLen = len(doc)
        tf = dict()
        for w in doc:
            tf[w] = doc[w] / docLen
        tf_word.append(tf)
    return tf_word

# 统计每个词在哪些文本中出现过
def countWinDoc(data):
    countDic = dict()
    for i, v in enumerate(data):
        for w in v:
            if not countDic.get(w):
                countDic[w] = set()  # 用set是为了去重
            countDic[w].add(i)
    return countDic
# 计算idf的值
def idf(data, docLen):
    idfDic = dict()
    for d in data:
        idfDic[d] = math.log(docLen / len(data[d]))  # data[d]+1，加1是为了防止分母为0
    return idfDic

# 计算每个文本中每个词的tfidf的值
def getTFIDF(tf, idf):
    tfidf = list()
    for t in tf:
        _tfidf = dict()
        for w in t:
            _tfidf[w] = 1.0 * t[w] * idf[w]
        tfidf.append(_tfidf)
    return tfidf

# TFIDF测试
def testTfIdf():
    
    s = ["我喜欢苹果，你喜欢吗？",
         "每天一个苹果，医生远离你",
         "永远不要拿苹果和橘子比较",
         "相对于橘子而言，我更喜欢苹果"]
    
    # 为每段文本实现分词
    cut_s = list()
    for i, v in enumerate(s):
        cut_s.append(fenci(v))
#     print(cut_s)
    # 统计每个文本中每个词出现的次数
    tfCount = getCount(cut_s)
    # 计算tf
    tf_result = tf(tfCount)
    # 统计每个词在哪些文档中出现过
    idfCount = countWinDoc(cut_s)
    # 计算idf的值
    idf_result = idf(idfCount, len(s))
    # 计算tf-idf
    tfIdf = getTFIDF(tf_result, idf_result)
    print(tfIdf)

# 构建每个文本的特征向量
def wordToFeature(s, sAll):
    indexF = [0] * len(sAll)
    for i in s:
        if i in sAll:
            indexF[sAll.index(i)] = 1
    return indexF

# 测试余弦距离
def testCosAB(a, b):
    top = sum([i * j for i, j in zip(a, b)])
    buttom = math.sqrt(sum(i * i for i in a)) * math.sqrt(sum(i * i for i in b))
    print(1.0 * top / buttom)   

if __name__ == '__main__':
    testTfIdf()













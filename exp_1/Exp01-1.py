# _*_ coding: utf-8 _*_
# author：chr

import os
from collections import Counter

# 要读取文件名为text，并位于当前路径
fileName = 'text.txt'

# 当前进程工作目录
dirName = os.getcwd()
fname = os.path.join(dirName, fileName)

with open(fname) as f:
    s = f.read()

# 将s字符串中的回车符转化成空格
# split 通过指定分隔符对字符串进行切片

'''
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。
计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。
'''
# 将多余的符号进行代换
temp = s.replace('.', ' ')
temp2 = temp.replace('(', ' ')
temp3 = temp.replace(')', ' ')
temp4 = temp3.replace(',', ' ')
counter = Counter(temp4.replace('\n', ' ').split(' '))

'''
# 声明一个格式化函数format
# 格式化要输出的每行数据，尾占20位，首占2位
'''
def format(a, b):
    return "{:<20}""{:>2}".format(a, b) + '\n'


title = format('词', '出现次数')
results = []


'''
# 要输出的数据，每一行由：词、频率+'\n'构成，序号=List.index(element)+1
counter 是字符串
most.common(n) 返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的。
'''
for w, c in counter.most_common():
    results.append(format(w, c))

# 将统计结果写入文件text_out.txt中
writefile = 'text_out.txt'
wpath = os.path.join(dirName, writefile)
with open(wpath, 'w') as f:
    f.write(''.join([title] + sorted(results)))

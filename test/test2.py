# -*- coding:utf-8 -*-
import os
import re

from homework import alignment


# def geshi(a, b):
#     return alignment(str(a)) + alignment(str(b), 18) + '\n'
#
# title = geshi('word', 'frequency')

path = 'text.txt'
results = []

with open(path, 'r') as f:
  word_list = []
  word_reg = re.compile(r'\w+')
  for line in f:
    line_words = line.split()
    word_list.extend(line_words)
  word_set = set(word_list) # 避免重复查询
  words_dict = {word: word_list.count(word) for word in word_set}
  for k, v in words_dict.items():
    print(k, v)




    # results.append(geshi(i, k, v))

# 返回当前工作目录
# dirname = os.getcwd();
# writefile = 'ar.txt'
# wpath = os.path.join(dirname, writefile)
# with open(wpath, 'w') as f:
#     f.write(''.join([title] + results))


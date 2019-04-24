
# -*- coding:utf-8 -*-
import collections
import re

# path = 'text.txt'
# with open(path, 'r') as f:
#     word_list = []
#     word_reg = re.compile(r'\w+')
#     for line in f:
#         line_words = line.split()
#         word_list.extend(line_words)
#     words_dict = dict(collections.Counter(word_list))
#     for k, v in words_dict.items():
#         print(k, v)

# 判断是否是闰年
# year = int(input("请输入一个年份: "))
# if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
#     print('{0} 是闰年' .format(year))
#     print()
#     print('{0} 是闰年' .format(year))
#
# else:
#     print('{0} 不是闰年' .format(year))
#     print()
#     print('{0} 是闰年' .format(year))

# 打印九九乘法表
# for i in range(1, 10):
#         for j in range(1, i+1):
#             # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
#             print('{}x{}={}\t'.format(i, j, i*j), end='')
#         print()


chr = str(input("qing shu ru: "))
print('dasf'.format(chr))
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

import re
# text.txt进行处理, 去除词性标注以、日期及一些杂质. (保留段落结构)
# 输入:text.txt
# 输出:newText.txt

def pre_file(filename):
    print("读取文件%r....."%filename)
    src_data = open(filename).read()

    # 去除词性标注、‘19980101-01-001-001’、杂质如‘[’、‘]nt’
    des_data =re.compile(r'(\/\w+)|(\d+\-\S+)|(\[)|(\]\S+)').sub('',src_data)
    des_filename = "text_new.txt"
    print("正在写入文件%r....."%des_filename)
    open(des_filename,'w').writelines(des_data)
    print("处理完成!")


# 建立倒排索引
# 输入:text.txt
# 输出:my_index.txt  格式(从0开始): word (段落号,段落中位置) ..
def create_inverted_index(filename):
    print("读取文件%r....."%filename)
    str_data = open(filename).read()
    # 变量说明
    sub_list = [] # 所有词的list,  用来查找去重等
    word = []     # 词表文件
    result = {}   # 输出结果 {单词:index}

    # 建立词表
    words_data = str_data.split()

    # 去重复(set:构建惟一元素的无序集合。)
    set_data = set(words_data)

    # set转换成list, 否则不能索引
    word = list(set_data)

    # 分割成单段话
    src_list = str_data.split("\n")

    # 建立索引
    for w in range(0, len(word)):
        index = []  # 记录段落及段落位置 [(段落号,位置),(段落号,位置)...]
        for i in range(0, len(src_list)):  # 遍历所有段落
            sub_list = src_list[i].split()
            for j in range(0, len(sub_list)):  # 遍历段落中所有单词
                if sub_list[j] == word[w]:
                    index.append((i,j))
            result[word[w]] = index

    des_filename = "newText.txt"
    print("正在写入文件%r....."%des_filename)
    writefile = open(des_filename,'w')
    for k in result.keys():
        writefile.writelines(str(k)+str(result[k])+"\n")
    print("处理完成!")
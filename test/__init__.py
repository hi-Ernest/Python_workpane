import numpy as np
from wordcloud import WordCloud
import PIL.Image as image

def test():
    with open("E:\\Python_workpane\\test\\text.txt") as fp:
        text = fp.read()
        # print(text)
		# 读取磁盘上指定图片
		
		# np 数组将图片的像素点记录存储以向量的形式 即图片的形状大小
		# mask：遮罩图，字的大小布局和颜色都会依据遮罩图生成。
        mask = np.array(image.open("E:\\Python_workpane\\test\\chr4.jpg"))
		
		# generate:根据文本生成词云 
        wordcloud = WordCloud(
            mask=mask
        ).generate(text)
		
		# 以BMG格式展示
        image_produce = wordcloud.to_image()
        image_produce.show()

if __name__ == '__main__':
    test()
#import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def make_worldcloud(file_path):                               #对应的文件编码
    text_from_file_with_apath = open(file_path, 'r', encoding='UTF-8').read()
    wordlist_after_jieba = jieba.cut(text_from_file_with_apath,cut_all=False)
    wl_space_split = " ".join(wordlist_after_jieba)
    print(wl_space_split)
    backgroud_Image = plt.imread('D:/下载/123.jpg')#图片路径
    print('加载图片成功')
    '''设置词云样式'''
    stopwords = STOPWORDS.copy()
    stopwords.add("如果")#屏蔽词，可以多个
    wc = WordCloud(
        width = 1024,
        height = 768,
        background_color = 'white',#背景色
        mask = backgroud_Image,
        font_path = 'D:/下载/simsun.ttc',#字体文件
        max_font_size = 400,
        random_state = 50,
    )
    wc.generate_from_text(wl_space_split)#开始加载文字
    img_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func=img_colors)#字体颜色为背景图片的颜色
    plt.imshow(wc)#显示云词图
    plt.axis('off')#是否显示X轴，Y轴下标
    plt.show()#显示
    #获取模块所在的路径
    d = path.dirname(__file__)
    # os.path.join(): 将多个路径组合后返回
    #print(d)
    wc.to_file(path.join(d,"h11.jpg"))#生成图片名称
    print('生成云词成功')

make_worldcloud('D:/下载/22945.txt')#文件路径，需要生成云词的文本

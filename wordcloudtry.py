
from wordcloud import WordCloud
import jieba
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt

#from scipy.misc import imread
#mk=imread("pic.png")
txt=open("C:/Users/严宇澄/Desktop/沉默的羔羊.txt","rt",encoding='UTF-8').read()

#print(" ".join(jieba.lcut(txt)))

mask=np.array(Image.open("C:/Users/严宇澄/Desktop/test.jpg"))
w=WordCloud(mask=mask,background_color="white",font_path="simkai.ttf",max_words=100000,colormap="BuPu")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pythoncloud.png")
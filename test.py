
from wordcloud import WordCloud
import jieba
font=
text_from_file_with_apath = open("C:/Users/严宇澄/Desktop/梦.docx","rt",encoding='ISO-8859-1').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)
my_wordcloud.to_file("pythoncloud.png")

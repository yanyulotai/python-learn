
'''wordcloud.WordCloud() ����һ���ı���Ӧ�Ĵ���
�ɸ����ı��д�����ֵ�Ƶ�ʵȲ������ƴ���

w = wordcloud.WordCloud()
������
1:w.generate(txt) :��WordCloud�����м����ı�txt
w.generate('python and WordClouod')
2:w.to_file(filename) :���������Ϊͼ���ļ���.png��.jpg��ʽ
w.to_file('outfile.png')
������
1��width:ָ�����ƶ�������ͼƬ�Ŀ�ȣ�Ĭ��400����
w = wordcloud.WordCloud(width = 600)
2��height: ָ�����ƶ�������ͼƬ�ĸ߶ȣ�Ĭ��200����
w=wordcloud.WordCloud(height=400)

���ö��������
1:min_font_size:ָ���������������С�ֺţ�Ĭ��4��
w = wordcloud.WordCloud(min_font_size = 10)
2:max_font_size:ָ�����������������ֺţ����ݸ߶��Զ�����
w = wordcloud.WordCloud(max_font_size=20)
3:font_size:ָ�������������ֺŵĲ��������Ĭ��Ϊ1
w = wordcloud.WordCloud(font_step=2)
4:font_path:ָ�������ļ���·����Ĭ��None
w = wordcloud.WordCloud(font_path='msyh.ttc')--΢���ź�
5:max_words:ָ��������ʾ����󵥴�������Ĭ��200
w = wordcloud.WordCloud(max_words=20)
6:stop_words:ָ�����Ƶ��ų����б�������ʾ�ĵ����б�
w = wordcloud.WordCloud(stop_words={'python'})
7:mask:ָ��������״��Ĭ��Ϊ�����Σ���Ҫ����imread()����
from scipy.misc import imread
mk = imread('pic.png')
w =  wordcloud.WordCloud(mask=mk)
8:background_color:ָ������ͼƬ�ı�����ɫ��Ĭ��Ϊ��ɫ
w = wordcloud.WordCloud(background_color='white')


wordcloud�ⳣ�淽��
����1�����ö������
����2�����ش����ı�
����3����������ļ�
'''
import wordcloud
c = wordcloud.WordCloud()
c.generate('wordcloud by python lalalala')
c.to_file('pywordcloud.png')

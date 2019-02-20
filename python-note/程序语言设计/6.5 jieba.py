#pip install jieba
'''
jieba分词原理：jieba分词依靠中文词库
1：利用一个中文词库，确定汉字之间的关联概率
2：汉字间概率大的组成词组，形成分词结果
3：除了分词，用户还可以添加自定义的词组
'''
#jieba分词3种模式
#1：精确模式：把文本精确的切分开，不存在冗余单词
jieba.lcut(s)
jieba.lcut('中国是一个伟大的国家')
['中国', '是', '一个', '伟大', '的', '国家']

#2：全模式：把文本中所有可能的词语都扫描出来，有冗余
jieba.lcut(s,cut_all=True)
jieba.lcut('中国是一个伟大的国家',cut_all=True)
['中国', '国是', '一个', '伟大', '的', '国家']

#3：搜索引擎模式：在精确模式基础上，对长词再次切分
jieba.lcut_for_search('中华人民共和国是伟大的')
['中华', '华人', '人民', '共和', '共和国', '中华人民共和国', '是', '伟大', '的']

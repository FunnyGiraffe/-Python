# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/14 10:00:21
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   统计文章中单词出现的次数
@File    :   ch7_5.py
'''
'''

'''
# here put the import lib

wordString = '''
    it was the best of times it was the worst of times.
    it was the age of wisdom it was the age of foolishness.
    the quick brown fox jumps over the lazy dog.
    '''
# 去除标点符号
wordString = wordString.replace('.','')
# 去除空格及其他特殊符号，将文本转换为单词列表
wordString = wordString.split()
wordFreq = []
for w in wordString:
    wordFreq.append(wordString.count(w))

# 用zip函数打包两个列表为元组：wordString: wordFreq
wordDict = dict(zip(wordString, wordFreq))
print(wordDict)
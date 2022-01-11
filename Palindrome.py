# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/11 14:49:24
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   判断一个数是否是回文数，将输入的数字转化为字符串，用正、负索引分别从头、尾比较；
             用到的知识点：while-else循环；跳出循环；序列索引
@File    :   Palindrome.py
'''

# here put the import lib
palindromeNum = str(input("请输入要判断的数："))
i = 0
j = -1
while i < len(palindromeNum) / 2:
    if palindromeNum[i] == palindromeNum[j]:
        i += 1
        j -= 1
    else:
        print('%s不是回文数!' %palindromeNum)
        break
else:
    print('%s是回文数!' %palindromeNum)
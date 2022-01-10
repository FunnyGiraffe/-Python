# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/10 10:34:56
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   if
@File    :   ch5_1_1.py
'''

# here put the import lib
score = int(input("Please input a num between 0~100: "))
if score >= 85:
    print("Excellent!")
if score < 60:
    print("你需要加倍努力！")
if (score >= 60) and (score < 85):
    print("还不错，仍需努力！")
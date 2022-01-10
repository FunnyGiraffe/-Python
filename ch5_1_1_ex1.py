# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/10 10:43:45
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   if-else
@File    :   ch5_1_1_ex1.py
'''

# here put the import lib
score = int(input("Please input a number between 0~100:"))
if score >= 60:
    if score >= 85:
        print("Excellent!")
    else:
        print("还不错，仍需努力！")
else:
    print("你需要加倍努力！")
# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/10 11:07:05
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   if-elif-else
@File    :   ch5_1_1_ex2.py
'''

# here put the import lib
score = int(input("Please input a number between 0~100:"))

if score >= 85:
    print("Excellent!")
elif score >= 60:
    print("还不错，但仍需努力！")
else:
    print("你需要加倍努力！")
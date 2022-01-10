# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/09 23:20:58
@Author  :   funnygiraffe 
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   水仙花数-while循环版
@File    :   ch5_1_1.py
'''

# here put the import lib
i = 100
while i < 1000:

    op = i%10   # one place
    tp = i//10 % 10     # ten place
    hp = i//100 % 10    # hundreds place
    if i == op**3 + tp**3 + hp**3:
        print("%i是水仙花数！" %i)
    i += 1
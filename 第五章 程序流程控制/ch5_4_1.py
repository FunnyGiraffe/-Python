#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ch5_4_1.py
@Time    :   2022/01/10 23:19:15
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2020, funnygiraffe
@Desc    :   水仙花数-for循环版
'''

# here put the import lib
for i in range(100,1000):
    op = i % 10
    tp = i // 10 % 10
    hp = i // 100
    if i == (op ** 3 + tp ** 3 + hp ** 3):
        print("%d是水仙花数." %i)
    i += 1
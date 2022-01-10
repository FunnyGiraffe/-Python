# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/10 16:58:50
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   水仙花数-for循环版
@File    :   ch5_4_1.py
'''

# here put the import lib
print("1000以内的水仙花数有:")
for i in range(100, 1000):
    op = i % 10     # one place
    tp = i//10 % 10  # ten place
    hp = i//100 % 10 # hundreds place
    if i == op ** 3 + tp ** 3 + hp ** 3:
        print(i)
    i += 1
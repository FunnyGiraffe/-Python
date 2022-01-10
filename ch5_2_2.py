# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/10 14:20:46
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   while-else
@File    :   ch5_2_2.py
'''

# here put the import lib
i = 0
while i * i < 1000:
    if i == 25:
        print("i=%d时break了，中途退出了while循环" %i)
        break
    i += 1
else:
    print("while循环正常结束，未出现break、return等终端循环的情况。")

print("i = %d" %i)
print("i * i = %d" %(i*i))
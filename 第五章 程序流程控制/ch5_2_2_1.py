# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/10 15:25:31
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   for-else，for循环正常结束后会执行else语句，若非正常结束(break、return等)则不执行else语句。
@File    :   ch5_2_2_1.py
'''

# here put the import lib
print("----字符串----")
s = input("请输入字符串：")
for item in s:
    print(item)
    if item == ' ':
        print("遇到空格了，break!中止for循环!")
        break
else:
    print("你输入的字符串没有空格，for循环完整结束!")
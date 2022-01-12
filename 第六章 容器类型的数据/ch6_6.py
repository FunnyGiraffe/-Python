# -*- encoding: utf-8 -*-
'''
@Time    :   2022/01/12 16:56:38
@Author  :   funnygiraffe
@Version :   1.0
@Contact :   funnygiraffe@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   遍历字典
@File    :   ch6_6.py
'''

# here put the import lib
s_dict = {102:"张三", 105:"李四", 109:"王五"}

print('----遍历键----')
for s_id in s_dict.keys():
    print('学号：' + str(s_id))

print('----遍历值----')
for s_name in s_dict.values():
    print('姓名：' + s_name)

print('----遍历键:值----')
for s_id, s_name in s_dict.items():
    print('学号:{0} 姓名:{1}'.format(s_id,s_name))
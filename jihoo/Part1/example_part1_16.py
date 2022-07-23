# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:13:02 2022

@author: user
"""

import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

ndf = df.set_index(['이름'])
print(ndf)
print('\n')

ndf2 = df.set_index(['음악'])
print(ndf2)
print('\n')

ndf3 = df.set_index(['수학', '음악'])
print(ndf3)
print('\n')
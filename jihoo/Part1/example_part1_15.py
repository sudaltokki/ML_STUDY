# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:10:27 2022

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

df = df.transpose()
print(df)
print('\n')

df = df.T
print(df)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

exam_data = {'수학' : [ 90,80,70], '영어' : [ 98, 89, 95], 
             '음악' : [ 85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])
print(df)
print('\n')

label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print('\n')
print(position1)

print('\n')

label2 = df.loc[['서준','우현']]
position2 = df.iloc[['0','1']]
print(label2)
print('\n')
print(position2)


print('\n')

label3 = df.loc['서준' : '우현']
position3 = df.iloc[0:1]
print(label3)
print('\n')
print(position3)

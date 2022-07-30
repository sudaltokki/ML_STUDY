# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 19:50:43 2022

@author: user
"""

import pandas as pd

df = pd.read_excel('C:\Python_exfiles\part6/주가데이터.xlsx', engine = 'openpyxl')
print(df.head(),'\n')
print(df.dtypes,'\n')

df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(dates.head(),'\n')

df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
print(df.head())
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:52:59 2022

@author: user
"""

import pandas as pd

file_path='./read_csv_sample.csv'

df1=pd.read_csv(file_path) #header 없으면 첫 행이 열 인덱스로 자동 설정
print(df1)
print('\n')

df2=pd.read_csv(file_path, header=None) #정수로 자동 설정
print(df2)
print('\n')

df3=pd.read_csv(file_path, index_col=None) #행 인덱스가 비어있음, 설정안하면 정수로 자동 설정 """
print(df3)
print('\n')

df4=pd.read_csv(file_path, index_col='c0') #c0열 원소를 행 인덱스로 지정
print(df4)
print('\n')

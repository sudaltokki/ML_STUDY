# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:40:12 2022

@author: user
"""

import pandas as pd

file_path = 'C:\\Python_exfiles\\part2/read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1)
print('\n')


df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')


df3 = pd.read_csv(file_path,index_col=None)
print(df3)
print('\n')


df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
print('\n')


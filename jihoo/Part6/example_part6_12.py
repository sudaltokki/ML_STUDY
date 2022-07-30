# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 00:19:05 2022

@author: user
"""

import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

df1 = pd.read_excel('C:\Python_exfiles\part6/stock price.xlsx', engine = 'openpyxl')
df2 = pd.read_excel('C:\Python_exfiles\part6/stock valuation.xlsx', engine = 'openpyxl')

print(df1)
print('\n')
print(df2)

merge_inner = pd.merge(df1, df2)
print(merge_inner)

merge_outer = pd.merge(df1, df2, how = 'outer', on = 'id')
print(merge_outer)

merge_left = pd.merge(df1, df2, how = 'left', left_on = 'stock_name', right_on = 'name')
print(merge_left)

merge_right = pd.merge(df1, df2, how = 'right', left_on = 'stock_name', right_on = 'name')
print(merge_right)

price = df1[df1['price'] < 50000]
print(price.head())
print('\n')

value = pd.merge(price, df2)
print(value)
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 00:32:33 2022

@author: user
"""

import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.unicode.east_asian_width', True)

df1 = pd.read_excel('C:\Python_exfiles\part6/stock price.xlsx', 
                    index_col = 'id', engine = 'openpyxl')
df2 = pd.read_excel('C:\Python_exfiles\part6/stock valuation.xlsx', 
                    index_col = 'id', engine = 'openpyxl')

df3 = df1.join(df2)
print(df3)

df4 = df1.join(df2, how = 'inner')
print(df4)
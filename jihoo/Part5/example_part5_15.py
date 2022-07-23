# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 09:36:45 2022

@author: user
"""

import pandas as pd

df = pd.read_csv('C:\\Python_exfiles\\part5/stock-data.csv')

print(df.head())
print('\n')
print(df.info())

df['new_Date'] = pd.to_datetime(df['Date'])

print(df.head())
print('\n')
print(df.info())

print('\n')
print(type(df['new_Date'][0]))

df.set_index('new_Date', inplace = True)
df.drop('Date', axis = 1, inplace = True)

print(df.head())
print('\n')
print(df.info())
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:16:15 2022

@author: user
"""

import pandas as pd

df = pd.read_csv('C:\\Python_exfiles\\part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

print(df.head())
print('\n')
print(df.tail())

print(df.shape)
print(df.info())

print(df.dtypes)
print('\n')
print(df.mpg.dtypes)

print(df.describe())
print('\n')
print(df.describe(include='all'))
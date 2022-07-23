# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 09:31:37 2022

@author: user
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Python_exfiles\\part5/auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset = ['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print(df.horsepower.describe())
print('\n')

df.horsepower = df.horsepower/abs(df.horsepower.max())

print(df.horsepower.head())
print('\n')
print(df.horsepower.describe())
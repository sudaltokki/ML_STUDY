# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 09:29:25 2022

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

count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)

bin_names = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x=df['horsepower'],
                      bins = bin_dividers,
                      labels = bin_names,
                      include_lowest=True)

horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:35:56 2022

@author: user
"""

import pandas as pd

df = pd.read_csv('C:\\Python_exfiles\\part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

print(df.count())
print('\n')

print(type(df.count()))

unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')

print(type(unique_values))

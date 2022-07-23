# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 09:03:30 2022

@author: user
"""

import pandas as pd

df = pd.read_csv('C:\\Python_exfiles\\part5/auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']
print(df.head(3))
print('\n')

mpg_to_kpl = 1.60934/3.78541

df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head(3))
print('\n')

df['kpl'] = df['kpl'].round(2)
print(df.head(3))

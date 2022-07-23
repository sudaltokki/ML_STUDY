# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:47:02 2022

@author: user
"""

import pandas as pd

df = pd.read_csv('C:\\Python_exfiles\\part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())

print(df.median())
print('\n')
print(df['mpg'].median())

print(df.max())
print('\n')
print(df['mpg'].max())

print(df.min())
print('\n')
print(df['mpg'].min())

print(df.std())
print('\n')
print(df['mpg'].std())

print(df.corr())
print('\n')
print(df[['mpg', 'weight']].corr())

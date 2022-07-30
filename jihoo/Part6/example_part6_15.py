# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 00:57:44 2022

@author: user
"""
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

std_all = grouped.std()
print(std_all)
print('\n')
print(type(std_all))
print('\n')

std_fare = grouped.fare.std()
print(std_fare)
print('\n')
print(type(std_fare))

def min_max(x):
    return x.max() - x.min()

agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())

agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
print('\n')

agg_sep = grouped.agg({'fare' : ['min', 'max'], 'age':'mean'})
print(agg_sep.head())